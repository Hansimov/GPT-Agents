import os
import shutil
from gpt4all import GPT4All
from utils import init_os_envs
from termcolor import colored

init_os_envs()


class OrcaMini3BAgent:
    def __init__(self, model_name=None, streaming=True):
        if model_name:
            self.model_name = model_name
        else:
            self.model_name = "orca-mini-3b.ggmlv3.q4_0.bin"
        self.streaming = streaming
        self.chat_seg = "$$$"
        self.init_prompts = {
            "chat": {
                "role": "system",
                "content": f"I will provide you some chats from different roles, each conversation with '{self.chat_seg} <Role>'. You should complete the chat based on whole conversation.\n",
            }
        }
        # self.messages = [self.init_prompts["chat"]]
        self.messages = []

    def load_model(self):
        self.model = GPT4All(model_name=self.model_name)

    def ask(self, message=None):
        """One-time Ask and Answer"""
        self.load_model()
        if not message:
            message = "Provide me a plan and necessary components for creating a World Simulator"
        output = self.model.generate(message)
        return output

    def simulate_chat_prompt(self, prompt, role="human", assistant_role="assistant"):
        chat_prompt = ""
        for message in self.messages:
            chat_prompt += f"{self.chat_seg} {message['role'].capitalize()}: {message['content']}\n"

        chat_prompt += f"{self.chat_seg} {role.capitalize()}: {prompt}\n"
        chat_prompt += f"{self.chat_seg} {assistant_role.capitalize()}:"

        # print(chat_prompt)
        return chat_prompt

    def stream_generate(self, prompt):
        for token in self.model.generate(prompt=prompt, top_k=1, streaming=True):
            yield token
            # print(token)

    def chat(self):
        """Interactive Chat"""
        self.load_model()
        prompts = [
            "Provide me a 5-step plan and necessary components for creating a World Simulator",
            "For last step, provide more details",
            "Criticize the details for last step, then provide three suggestions on how to improve it",
            "How many rounds of the chats in above conversation?",
        ]

        for prompt in prompts:
            print(colored(prompt, "cyan"))
            chat_prompt = self.simulate_chat_prompt(prompt)
            response = []
            if self.streaming:
                for token in self.model.generate(
                    prompt=chat_prompt,
                    top_k=1,
                    max_tokens=300,
                    streaming=True,
                ):
                    print(colored(token, "green"), end="")
                    response.append(token)
                print()

            else:
                response = self.model.generate(chat_prompt)
                print(response)

            self.messages.extend(
                [
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": "".join(response)},
                ]
            )

            print(shutil.get_terminal_size()[0] * "-")

    def run(self):
        self.chat()
