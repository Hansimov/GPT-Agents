import asyncio
import concurrent.futures


# python -m pip install windows-curses
import curses
import platform
import random
import shutil
import sys
import textwrap
import time

if platform.system() == "Windows":
    from ctypes import windll

    windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)


class LLMAgent:
    def __init__(self, model="ChatGPT"):
        self.model = model
        # self.word_num = random.randint(20, 30)
        self.word_num = 30
        self.msg = f"[{self.model}]: I am {self.model}. ({self.word_num} words) "
        # self.msg_to_lines()
        self.count_msg_lines()

    def msg_to_lines(self):
        self.lines = textwrap.wrap(
            self.msg,
            width=shutil.get_terminal_size().columns,
        )

    def count_msg_lines(self):
        terminal_width = shutil.get_terminal_size().columns
        self.line_num = int(len(self.msg) / terminal_width) + 1

    async def answer(self, question=None):
        line_num = self.line_num
        print(self.msg, end="", flush=True)
        for i in range(self.word_num):
            new_msg = f"<{self.model}_word_{i}>"
            self.msg += new_msg
            # self.msg_to_lines()
            self.count_msg_lines()
            rand_num = random.random() * 0.1
            await asyncio.sleep(rand_num)
            async with self.task_runner.lock:
                self.task_runner.lock_counter += 1
                print(new_msg, end="", flush=True)
                if line_num == self.line_num:
                    # print(self.lines[line_num - 1], end="\r")
                    pass
                else:
                    # print(self.line_num)
                    # print(self.lines[line_num], end="\r")
                    # # for i in range(line_num):
                    # #     print("\033[F")
                    # # print("\033[K", end="\r")
                    # for line in self.lines[line_num:]:
                    #     print(f"{line}")
                    line_num = self.line_num
        print()

        #     for line in self.lines:
        #         print(f"\033[K{line}")
        # for i in range(len(self.lines) + 1):
        #     print("\033[F")
        # print()
        # print(self.lines, "\r")
        # print(f"\033[K{self.msg}", end="\r")


class TaskRunner:
    def __init__(self):
        self.lock = asyncio.Lock()
        self.agents = []
        self.lock_counter = 0

    def console_output(self):
        msg = ""
        for agent in self.agents:
            msg += agent.msg
        print(msg + "\r")

    async def ask_question(self, question="Hello, who are you?"):
        print(question)
        models = [
            "ChatGPT",
            "Sage",
            # "Claude-instant",
            # "Claude-instant-100k",
            # "Claude+",
            # "Bing",
        ]
        agents = [LLMAgent(model) for model in models]
        for i, agent in enumerate(agents):
            agent.task_runner = self
            self.agents.append(agent)
        tasks = [asyncio.create_task(agent.answer(question)) for agent in agents]
        await asyncio.gather(*tasks)

    def run(self):
        asyncio.run(self.ask_question())


task_runner = TaskRunner()
task_runner.run()
