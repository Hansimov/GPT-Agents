import hashlib
import json
import logging
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
from termcolor import colored
from datetime import datetime

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

            response = self.save_message(event_data)

            return jsonify(response)

    def save_message(self, event_data):
        chat_dumper = ChatDumper()
        chat_dumper.add_message(event_data)
        return {"message": "Saved!"}

    def run(self):
        self.app.run(
            debug=True,
            host=self.host,
            port=self.port,
        )


class ChatDumper:
    chat_json_path = (
        Path(__file__).parent / "webpage" / "src" / "data" / "vue_chats.json"
    )
    message_id = 0

    def __init__(self):
        with open(self.chat_json_path, "r") as rf:
            self.chat_data = json.load(rf)

    def dump(self):
        with open(self.chat_json_path, "w") as wf:
            json.dump(self.chat_data, wf, indent=4)

    def add_message(self, message):
        message_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        message_timestamp = str(int(datetime.now().timestamp()))
        # message_id = hashlib.md5(message_timestamp.encode("utf-8")).hexdigest()
        message_id = message_timestamp
        sender_id = "0"
        room_id = message["roomId"]
        new_message = {
            "_id": message_id,
            "senderId": sender_id,
            "content": message["content"],
            # "date": message_datetime,
            "timestamp": message_datetime,
            "replyMessage": {},
        }
        self.chat_data["roomMessages"][room_id].append(new_message)
        self.dump()


if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run()
