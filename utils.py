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


# python -m pip install EdgeGPT --upgrade
# from EdgeGPT.EdgeGPT import Chatbot
from EdgeGPT.EdgeUtils import Query, Cookie


def init_os_envs(set_proxy=True, apis=["openai", "bard", "claude"]):
    with open(Path(__file__).parent / "secrets.json", "r") as rf:
        secrets = json.load(rf)

    if set_proxy:
        for proxy_env in ["http_proxy", "https_proxy"]:
            os.environ[proxy_env] = secrets["http_proxy"]

    if type(apis) == str:
        apis = [apis]
    apis = [api.lower() for api in apis]

    if "openai" in apis:
        os.environ["OPENAI_API_KEY"] = secrets["openai_api_key"]
        openai.api_key = os.environ["OPENAI_API_KEY"]

    if "bard" in apis:
        os.environ["BARD_API_KEY"] = secrets["bard_api_key"]

    if "claude" in apis:
        os.environ["CLAUDE_API_KEY"] = secrets["claude_api_key"]


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
