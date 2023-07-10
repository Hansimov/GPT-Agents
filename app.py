import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

logging.getLogger().setLevel(logging.INFO)


app = Flask(__name__)
CORS(app)


@app.route("/message", methods=["POST"])
def handle_event():
    logging.info("Receiving ...")
    event_data = request.get_json()
    logging.info("Received.")

    logging.info(event_data)
    result = generate_message(event_data)

    return jsonify(result)


def generate_message(event_data):
    return {"message": "Received!"}


if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=8888)
    app.run(debug=True, host="127.0.0.1", port=8888)
