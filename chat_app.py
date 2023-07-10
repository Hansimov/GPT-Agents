import hashlib
import json
import logging
import re
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from pathlib import Path
from termcolor import colored
from datetime import datetime

# logging.getLogger().setLevel(logging.INFO)


def generate_message_from_content(content, sender_id="0"):
    message_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    message_timestamp = str(datetime.now().timestamp())
    # message_id = hashlib.md5(message_timestamp.encode("utf-8")).hexdigest()
    message_id = message_timestamp
    # room_id = message["roomId"]
    message = {
        "_id": message_id,
        "senderId": sender_id,
        "content": content,
        # "date": message_datetime,
        "timestamp": message_datetime,
        "replyMessage": {},
    }
    return message


class ChatApp:
    host = "127.0.0.1"
    port = 8888

    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.register_routes()
        self.chat_dumper = ChatDumper()

    def register_routes(self):
        @self.app.route("/message", methods=["POST"])
        def handle_event():
            print(colored("Receiving ...", "cyan"))
            message = request.get_json()
            print(colored(message, "yellow"))
            print(colored("Received.", "green"))

            response = self.save_message(message)
            if "usersTag" in message and message["usersTag"]:
                receiver_ids = [user["_id"] for user in message["usersTag"]]
                self.talk_to(receiver_ids, message)
            return jsonify(response)

    def save_message(self, message):
        self.chat_dumper.add_message(message)
        return {"message": "Saved!"}

    def talk_to(self, receiver_ids, message):
        room_id = message["roomId"]
        content = message["content"]
        plain_text = re.sub(r"<usertag>.*?</usertag>", "", content).strip()
        for receiver_id in receiver_ids:
            reply_content = (
                f"Reply [{plain_text}] from <usertag>{receiver_id}</usertag>"
            )
            reply_message = generate_message_from_content(
                reply_content,
                sender_id=receiver_id,
            )
            self.chat_dumper.add_message(
                reply_message, sender_id=receiver_id, room_id=room_id
            )
            time.sleep(0.2)

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
        self.load()

    def load(self):
        with open(self.chat_json_path, "r") as rf:
            self.chat_data = json.load(rf)

    def dump(self):
        with open(self.chat_json_path, "w") as wf:
            json.dump(self.chat_data, wf, indent=4)

    def add_message(self, message, sender_id="0", room_id=None):
        if room_id is None:
            room_id = message["roomId"]
        new_message = generate_message_from_content(message["content"], sender_id)
        self.chat_data["roomMessages"][room_id].append(new_message)
        self.dump()


class Chatter:
    def __init__(self):
        pass


if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run()
