import os
from gpt4all import GPT4All
from utils import init_os_envs

init_os_envs()


class OrcaMini3BAgent:
    def __init__(self, llm_bin=None):
        if llm_bin:
            self.llm_bin = llm_bin
        else:
            self.llm_bin = "orca-mini-3b.ggmlv3.q4_0.bin"

    def load_model(self):
        self.model = GPT4All(model_name=self.llm_bin)

    def ask(self, message=None):
        """One-time Ask and Answer"""
        self.load_model()
        if not message:
            message = "Provide me a plan and necessary components for creating a World Simulator"
        output = self.model.generate(message)
        return output

    def chat(self, stream=True):
        """Interactive Chat"""
        self.load_model()
        with self.model.chat_session():
            response = self.model.generate(
                prompt="Provide me a 5-step plan and necessary components for creating a World Simulator",
                top_k=1,
            )
            response = self.model.generate(
                prompt="For last step, provide more details",
                top_k=1,
                max_tokens=300,
            )
            response = self.model.generate(
                prompt="Criticize the details for last step, then provide three suggestions on how to improve it",
                top_k=1,
                max_tokens=300,
            )

            print(self.model.current_chat_session)

    def run(self):
        self.chat()
