import json
import random
import time
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from pymongo import MongoClient
from agents.chimera_agent import ChimeraAgent
from managers.chat_message_manager import ChatMessageManager


class AgentsApp:
    host = "127.0.0.1"
    port = 8888

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.register_routes()

    def register_routes(self):
        self.route_func_dict = {
            ("/api/chat", "POST"): self.chat,
        }
        for route, func in self.route_func_dict.items():
            self.app.route(route[0], methods=[route[1]])(func)

    def stream_response_generator(self, response_message):
        index = 0
        for key, value in response_message.items():
            if key == "content":
                content_chunks = value.split()
                for chunk in content_chunks:
                    delta = {"content": f" {chunk}"}
                    delta_json = (
                        json.dumps(
                            {"delta": delta, "finish_reason": None, "index": index}
                        )
                        + "\n"
                    )
                    index += 1
                    print(delta_json, flush=True)
                    time.sleep(random.random() * 0.1)
                    yield delta_json
            else:
                time.sleep(random.random() * 0.1)
                delta = {key: value}
                yield json.dumps(
                    {"delta": delta, "finish_reason": None, "index": index}
                ) + "\n"
                index += 1
        last_message = {
            "delta": {"content": ""},
            "finish_reason": "stop",
            "index": index,
        }
        yield json.dumps(last_message) + "\n"

    def chat(self):
        message = request.get_json()
        print(message)
        response_message = {
            "status": "ok",
            "content": f"Hi, I'm Chimera Agent! Reply to: [{message['content']}]",
        }
        print(response_message)
        response = Response(self.stream_response_generator(response_message))
        return response

    def run(self):
        self.app.run(host=self.host, port=self.port, debug=True)


def main():
    agents_app = AgentsApp()
    agents_app.run()


if __name__ == "__main__":
    main()
