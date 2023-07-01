import asyncio
import datetime
import json
import logging
import os
import platform
import shutil
import sys


from pathlib import Path
from termcolor import colored


# python -m pip install --upgrade openai
import openai


# python -m pip install poe-api
import poe

# poe.logger.setLevel(logging.INFO)

# python -m pip install EdgeGPT --upgrade
# from EdgeGPT.EdgeGPT import Chatbot
from EdgeGPT.EdgeUtils import Query, Cookie


def init_os_envs():
    with open(Path(__file__).parent / "secrets.json", "r") as rf:
        secrets = json.load(rf)

    for proxy_env in ["http_proxy", "https_proxy"]:
        os.environ[proxy_env] = secrets["http_proxy"]

    os.environ["OPENAI_API_KEY"] = secrets["openai_api_key"]
    os.environ["BARD_API_KEY"] = secrets["bard_api_key"]
    os.environ["CLAUDE_API_KEY"] = secrets["claude_api_key"]
    openai.api_key = os.environ["OPENAI_API_KEY"]


# init_os_envs()


class ContextManager:
    def __init__(self):
        self.chat_history = []
        request_body = {
            "model": None,
            "question": None,
            "datetime": None,
        }


class ChatResponse:
    def __init__(self):
        self.question = None


class ChatRequest:
    def __init__(self, question, model):
        self.question = question
        self.model = model
        self.datetime = datetime.datetime.now()


class ChatGPTAgent:
    """
    * openai-cookbook: How to format inputs to ChatGPT models
      * https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb
    """

    def __init__(
        self,
        original_text,
        model="gpt-3.5-turbo",
        task="en2zh",
    ):
        task_system_message_dict = {
            "en2zh": "你是一个英译中翻译专家。你的任务是将给定的英文如实翻译成中文。",
        }
        self.model = model
        self.system_message = task_system_message_dict[task]
        self.original_text = original_text

    def run(self):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.system_message,
                    "role": "user",
                    "content": self.original_text,
                },
            ],
            temperature=0,
        )

        self.translated_text = response["choices"][0]["message"]["content"]
        return self.translated_text


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


class BingAgent:
    def __init__(self):
        pass

    def run(self):
        cookie_file = Path(__file__).parent / "bing_cookies_main.json"
        q = Query(
            "Hello world",
            style="precise",
            proxy=os.environ["http_proxy"],
            cookie_file=cookie_file,
        )
        print(q.output)


if __name__ == "__main__":
    translater = ChatGPTAgent(
        "Evaluation of GPT-3.5 and GPT-4 for supporting real-world information needs in healthcare delivery"
    )
    translater.run()
    print(translater.translated_text)
