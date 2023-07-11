class InstructMessageManager:
    def __init__(self, system_message_style="chat", system_message_str=None):
        self.chat_seg = "$" * 3
        self.messages = []
        self.init_system_message(system_message_style, system_message_str)

    def init_system_message(self, system_message_style, system_message_str):
        self.system_message_styles = {
            "chat": {
                "role": "system",
                "content": f"I will provide you some chats from different roles, each conversation starts with '{self.chat_seg} [Role]'. You should complete the last chat based on whole conversation.\n",
            }
        }
        self.system_message_style = system_message_style
        self.system_message_str = system_message_str

        if system_message_style:
            self.messages.append(self.system_message_styles[system_message_style])
        elif system_message_str:
            self.messages.append({"role": "system", "content": system_message_str})

    def update_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def add_messages(self, message):
        if type(message) == list:
            self.messages.extend(message)
        elif type(message) == dict:
            self.messages.append(message)

    def full_chat_prompt(self, prompt, role="human", assistant_role="assistant"):
        chat_prompt = ""
        for message in self.messages:
            if message["role"] == "system":
                chat_prompt += f"{message['content']}"
            else:
                chat_prompt += f"{self.chat_seg} [{message['role'].capitalize()}]: {message['content']}\n"
        chat_prompt += f"{self.chat_seg} [{role.capitalize()}]: {prompt}\n"
        chat_prompt += f"{self.chat_seg} [{assistant_role.capitalize()}]:"

        return chat_prompt
