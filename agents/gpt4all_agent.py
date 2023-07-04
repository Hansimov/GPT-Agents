import os
import shutil
from pathlib import Path
from gpt4all import GPT4All
from utils import init_os_envs
from termcolor import colored
from managers import MessageManager

init_os_envs()


class GPT4AllAgent:
    model_path_root = str(Path(__file__).parents[1] / ".cache/gpt4all")

    def __init__(self, model_name=None, streaming=True):
        """
        GPT4All: https://gpt4all.io/index.html
        """
        self.valid_models = [
            "nous-hermes-13b.ggmlv3.q4_0.bin",  # Best overall model
            "ggml-model-gpt4all-falcon-q4_0.bin",  # Best overall smaller model
            "ggml-gpt4all-j-v1.3-groovy.bin",
            "GPT4All-13B-snoozy.ggmlv3.q4_0.bin",
            "ggml-mpt-7b-chat.bin",  # Best overall smaller model
            "orca-mini-7b.ggmlv3.q4_0.bin",
            "orca-mini-3b.ggmlv3.q4_0.bin",
            "orca-mini-13b.ggmlv3.q4_0.bin",
            "ggml-vicuna-7b-1.1-q4_2.bin",
            "ggml-vicuna-13b-1.1-q4_2.bin",
            "ggml-wizardLM-7B.q4_2.bin",
            "ggml-stable-vicuna-13B.q4_2.bin",
            "ggml-mpt-7b-instruct.bin",
            "ggml-mpt-7b-base.bin",
            "ggml-nous-gpt4-vicuna-13b.bin",
            "wizardLM-13B-Uncensored.ggmlv3.q4_0.bin",
            "ggml-replit-code-v1-3b.bin",
        ]
        if model_name:
            self.model_name = model_name
        else:
            self.model_name = "orca-mini-3b.ggmlv3.q4_0.bin"
        self.streaming = streaming
        self.message_manager = MessageManager()

    def load_model(self, model_name=None):
        if model_name:
            self.model_name = model_name

        self.model = GPT4All(
            model_name=self.model_name,
            model_path=self.model_path_root,
        )

    def ask(self, message=None):
        """One-time Ask and Answer"""
        self.load_model()
        output = self.model.generate(message)
        return output

    def chat(self, prompts=None):
        """Interactive Chat"""
        if not prompts:
            raise ValueError("No prompts!")
        if type(prompts) == str:
            prompts = [prompts]

        self.load_model()

        for prompt in prompts:
            print(colored(prompt, "cyan"))
            chat_prompt = self.message_manager.full_chat_prompt(prompt)
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

            self.message_manager.add_messages(
                [
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": "".join(response)},
                ]
            )

            print(shutil.get_terminal_size()[0] * "-")

    def run(self):
        self.chat()
