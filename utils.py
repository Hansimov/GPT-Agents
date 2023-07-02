import asyncio
import datetime
import json
import logging
import os
import platform
import shutil
import sys


from pathlib import Path


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


if __name__ == "__main__":
    translater = ChatGPTAgent(
        "Evaluation of GPT-3.5 and GPT-4 for supporting real-world information needs in healthcare delivery"
    )
    translater.run()
    print(translater.translated_text)
