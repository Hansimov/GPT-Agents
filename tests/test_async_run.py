import asyncio
import concurrent.futures
import random
import time


class LLMAgent:
    def __init__(self, model="ChatGPT"):
        self.model = model

    async def answer(self, question=None):
        msg = f"[{self.model}]: I am {self.model}. "
        print(msg)
        for i in range(5):
            rand_num = random.random() * 0.5
            msg += f"<{self.model}_holder_{round(rand_num,2)}>"
            await asyncio.sleep(rand_num)
            print(
                f"\033[{self.index}A\033[2K{msg}\033[{self.index}B",
                end="\r",
            )
        return msg


class TaskRunner:
    def __init__(self):
        pass

    async def ask_question(self, question="Hello, who are you?"):
        print(question)
        models = [
            "ChatGPT",
            "Sage",
            "Claude-instant",
            "Claude-instant-100k",
            "Claude+",
            "Bing",
        ]
        agents = [LLMAgent(model) for model in models]
        for i, agent in enumerate(agents):
            agent.index = len(models) - i
        tasks = [asyncio.create_task(agent.answer(question)) for agent in agents]
        await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self.ask_question())


task_runner = TaskRunner()
task_runner.run()
