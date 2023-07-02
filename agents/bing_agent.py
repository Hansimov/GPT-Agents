import os
import sys
import asyncio
import json
from pathlib import Path
from utils import init_os_envs

sys.path.insert(0, str(Path("E:/_codes/EdgeGPT/src")))
# python -m pip install EdgeGPT --upgrade
# from EdgeGPT.EdgeUtils import Query, Cookie

from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

init_os_envs("bing")


class BingAgent:
    def __init__(self):
        # self.cookie_file = Path(__file__).parents[1] / "bing_cookies_1.json"
        # with open(self.cookie_file, "r") as rf:
        #     self.cookies = json.load(rf)
        self.cookies = json.loads(
            open(
                Path(__file__).parents[1] / "bing_cookies_1.json", encoding="utf-8"
            ).read()
        )

    async def chat(self):
        self.bot = await Chatbot.create(
            cookies=self.cookies,
        )
        response = await self.bot.ask(
            prompt="Hello world",
            conversation_style=ConversationStyle.precise,
            simplify_response=True,
        )
        print(json.dumps(response, indent=2))

        # Returns
        """
        {
            "text": str,
            "author": str,
            "sources": list[dict],
            "sources_text": str,
            "suggestions": list[str],
            "messages_left": int
        }
        """
        await self.bot.close()

    def run(self):
        asyncio.run(self.chat())
