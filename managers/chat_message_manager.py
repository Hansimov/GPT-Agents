import re
from termcolor import colored
from agents.chimera_agent import output_stream_response


class ChatMessageManager:
    def __init__(self, multiple_chat_roles=True, lang="zh"):
        self.chat_seg = "" * 3
        self.chat_messages = []
        self.agents = []
        if lang == "zh":
            self.chat_roles_system_message = f"我会向你提供来自不同人的一些对话记录，每个对话以 `{self.chat_seg} [人物]:` 开头。你需要牢记自己的角色和身份，然后基于上下文作出相应的回应。你的回答不需要加上人物开头。"
        else:
            self.chat_roles_system_message = f"I will provide you some chats from different roles, each conversation starts with `{self.chat_seg} [Role]:`. You should keep in mind your own role, then response accordingly based on the context."
        self.term_colors = ["cyan", "green"]
        self.term_index = 0

    def cleanse_chat_content(self, chat_content):
        return re.sub(
            f"^\s*{self.chat_seg}\s*\[.*?\]:",
            "",
            chat_content,
            flags=re.MULTILINE,
        )

    def content_to_message(self, role, content):
        return {"role": role, "content": content}

    def add_agents(self, agents):
        if type(agents) == list:
            self.agents.extend(agents)
        else:
            self.agents.append(agents)

    def add_to_chat_messages(self, chat_message):
        if type(chat_message) == list:
            self.chat_messages.extend(chat_message)
        elif type(chat_message) == dict:
            self.chat_messages.append(chat_message)
        else:
            pass

    def construct_request_messages_from_chat_messages(
        self,
        current_role,
        current_role_system_content,
    ):
        request_messages = []
        current_role_system_message = {
            "role": "system",
            "content": current_role_system_content,
        }
        chat_roles_system_message = {
            "role": "system",
            "content": self.chat_roles_system_message,
        }
        request_messages.extend(
            [
                current_role_system_message,
                chat_roles_system_message,
            ]
        )
        for chat_message in self.chat_messages:
            role = chat_message["role"]
            content = chat_message["content"]
            suffixed_content = {
                "content": f"{self.chat_seg} [{role.capitalize()}]: {content}\n",
            }
            if role == "system":
                request_message = {"role": "system", **suffixed_content}
            elif role == current_role:
                request_message = {"role": "assistant", **suffixed_content}
            else:
                request_message = {"role": "user", **suffixed_content}
            request_messages.append(request_message)

        # To increase weights of system message
        request_messages.append(current_role_system_message)
        return request_messages

    def next_term_color(self):
        self.term_color = self.term_colors[self.term_index % len(self.term_colors)]
        self.term_index += 1
        return self.term_color

    def color_print_message(self, message, color=None):
        role = message["role"]
        content = message["content"]
        if color is None:
            role_color = "magenta"
            content_color = "cyan"
        else:
            role_color = color
            content_color = color
        print(f"[{colored(role, role_color)}]: {colored(content, content_color)}")

    def sequential_chat(self, init_content=None, rounds=1, stream_chat=True):
        if init_content:
            init_message = self.content_to_message("user", init_content)
            self.color_print_message(init_message, color="yellow")
            self.add_to_chat_messages(init_message)

        for i in range(rounds):
            for agent in self.agents:
                # print(f"chat_messages: {self.chat_messages}")
                current_request_messages = (
                    self.construct_request_messages_from_chat_messages(
                        agent.name,
                        agent.system_message,
                    )
                )
                # print(f"current_request_messages: {current_request_messages}")
                print(
                    f"[{colored(agent.name, self.next_term_color())}]: ",
                    end="",
                    flush=True,
                )

                response = agent.chat(current_request_messages, stream=stream_chat)

                current_role_chat_message = {"role": agent.name, "content": ""}

                if not stream_chat:
                    current_role_chat_content = self.cleanse_chat_content(
                        response["choices"][0]["message"]["content"]
                    )
                    current_role_chat_message["content"] = current_role_chat_content
                    print(f"{colored(current_role_chat_content, self.term_color)}")
                    # self.color_print_message(current_role_chat_message)
                else:
                    current_role_chat_message["content"] = output_stream_response(
                        response,
                        self.cleanse_chat_content,
                        content_color=self.term_color,
                    )

                self.add_to_chat_messages(current_role_chat_message)
