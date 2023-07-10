import logging
from termcolor import colored
from flask import Flask, request, jsonify
from flask_cors import CORS

# logging.getLogger().setLevel(logging.INFO)


class ChatApp:
    host = "127.0.0.1"
    port = 8888

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.register_routes()

    def register_routes(self):
        @self.app.route("/message", methods=["POST"])
        def handle_event():
            print(colored("Receiving ...", "cyan"))
            event_data = request.get_json()
            print(colored(event_data, "yellow"))
            print(colored("Received.", "green"))

            response = self.generate_message(event_data)

            return jsonify(response)

    def generate_message(self, event_data):
        return {"message": "Received!"}

    def run(self):
        self.app.run(
            debug=True,
            host=self.host,
            port=self.port,
        )


if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run()
