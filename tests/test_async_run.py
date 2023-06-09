import asyncio
import concurrent.futures
import random
import shutil
import textwrap
import time


class LLMAgent:
    def __init__(self, model="ChatGPT"):
        self.model = model

    async def answer(self, question=None):
        word_num = random.randint(20, 30)
        msg = f"[{self.model}]: I am {self.model}. ({word_num} words) "
        print(msg)
        for i in range(word_num):
            rand_num = random.random() * 0.3
            msg += f"<{self.model}_word_{i}>"
            await asyncio.sleep(rand_num)
            lines = textwrap.wrap(
                msg,
                width=shutil.get_terminal_size().columns,
            )
            self.task_runner.max_lines = max(self.task_runner.max_lines, len(lines))
            for j, line in enumerate(lines):
                index = self.index + j
                line = lines[j] if j < len(lines) else ""
                print(
                    f"\033[{index + j}A\033[2K{line}\033[{index + j}B",
                    end="\r",
                )
        return msg


class TaskRunner:
    def __init__(self):
        self.max_lines = 0

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
            agent.index = i * self.max_lines + 1
            agent.task_runner = self
        tasks = [asyncio.create_task(agent.answer(question)) for agent in agents]
        await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self.ask_question())


task_runner = TaskRunner()
task_runner.run()
