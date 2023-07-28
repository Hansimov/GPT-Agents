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

    def chat(self):
        message = request.get_json()
        print(message)
        response_message = {
            "status": "ok",
            "content": "Hi, I'm Chimera!",
        }
        print(response_message)
        return jsonify(response_message)

    def run(self):
        self.app.run(host=self.host, port=self.port, debug=True)


def main():
    agents_app = AgentsApp()
    agents_app.run()


if __name__ == "__main__":
    main()
