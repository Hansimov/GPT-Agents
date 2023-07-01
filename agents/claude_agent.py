from utils import init_os_envs
import os
import platform
import shutil
from termcolor import colored

# python -m pip install poe-api
import poe

# poe.logger.setLevel(logging.INFO)

init_os_envs("claude")


class ClaudeAgent:
    def __init__(self, model="Claude-instant"):
        self.poe_model_name_map = {
            "Sage": "capybara",
            "Claude-instant": "a2",
            "Claude-instant-100k": "a2_100k",
            "Claude+": "a2_2",
            "ChatGPT": "chinchilla",
            "GPT-4": "beaver",
        }
        self.poe_model_id_map = {v: k for k, v in self.poe_model_name_map.items()}

        self.model = model
        self.model_id = self.poe_model_name_map[model]
        # print(f"> Poe LLM Model: {self.model}")
        self.claude_client = poe.Client(
            token=os.environ["CLAUDE_API_KEY"],
            proxy=os.environ["http_proxy"],
        )

    def prompt(self, message):
        for chunk in self.claude_client.send_message(
            self.model_id,
            message,
            with_chat_break=True,
        ):
            print(chunk["text_new"], end="", flush=True)
        print()

    def get_history(self, count=5):
        history = self.claude_client.get_message_history(
            self.model_id,
            count=count,
        )
        if platform.system() == "windows":
            os.system("color")

        for message in history:
            author = message["node"]["author"]
            text = message["node"]["text"]
            if author == "chat_break":
                print("-" * shutil.get_terminal_size()[0])
            else:
                if author != "human":
                    author = self.poe_model_id_map[author]

                if author == "human":
                    text_color = "green"
                elif author != "chat_break":
                    text_color = "cyan"
                else:
                    text_color = "white"
                print(f"[{author}]: " f"{colored(text,text_color)}")
        print()

    def run(self):
        self.get_history(count=10)
        # self.prompt("Introduce yourself in less than 10 words.")
        # self.prompt("Repeat my last question.")
