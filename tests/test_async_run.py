import concurrent.futures
import random
import time


class LLMAgent:
    def __init__(self, model="ChatGPT"):
        self.model = model

    def answer(self, question=None):
        rand_num = random.randint(1, 4)
        msg = f"[{self.model}]: I am {self.model}. Sleeping {rand_num}s."
        time.sleep(rand_num)
        print(msg)
        return msg


class TaskRunner:
    def __init__(self):
        pass

    def ask_question(self, question="Hello, who are you?"):
        print(question)
        models = [
            "ChatGPT",
            "Sage",
            "Claude-instant",
            "Claude-instant-100k",
            "Claude+",
            "Bing",
        ]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            agents = [LLMAgent(model) for model in models]
            results = [executor.submit(agent.answer, question) for agent in agents]
            for f in concurrent.futures.as_completed(results):
                # print(f.result())
                pass

    def run(self):
        self.ask_question()


task_runner = TaskRunner()
task_runner.run()
