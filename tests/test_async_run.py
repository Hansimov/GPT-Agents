import asyncio
import concurrent.futures


# python -m pip install windows-curses
import curses
import random
import shutil
import textwrap
import time


class LLMAgent:
    def __init__(self, model="ChatGPT"):
        self.model = model
        self.lines_printed = 0

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
                index = self.index + j + self.lines_printed
                line = lines[j] if j < len(lines) else ""
                try:
                    curses.setupterm()
                    curses.putp(curses.tparm(curses.tigetstr("cuu"), index + j))
                    curses.putp(curses.tigetstr("el"))
                    print(line, end="\r")
                    curses.putp(curses.tparm(curses.tigetstr("cud"), index + j))
                except Exception as e:
                    print(f"Error: {e}")
            self.lines_printed += len(lines) - 1
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
