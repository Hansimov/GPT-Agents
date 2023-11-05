import {
    jsonize_stream_data,
    stringify_stream_bytes,
} from "./stream_jsonizer.js";
import { openai_api_key } from "./secrets.js";
import { update_chat, create_chat_block } from "./chat_renderer.js";

export function request_chat_completion() {
    var url =
        "https://corsproxy.io/?https://magic-api.ninomae.live/v1/chat/completions";
    var request_options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${openai_api_key}`,
        },
        body: JSON.stringify({
            model: "poe-gpt-3.5-turbo",
            messages: [
                {
                    role: "user",
                    content:
                        // "DO NOT SAY ANY OTHER THING. JUST REPEAT ONE WORD: 'hello'.",
                        "who are you?",
                },
            ],
            temperature: 0,
            stream: true,
        }),
    };
    create_chat_block("user", "who are you?");
    create_chat_block("assistant");

    fetch(url, request_options)
        .then((response) => response.body)
        .then((rb) => {
            const reader = rb.getReader();
            return reader.read().then(function process({ done, value }) {
                if (done) {
                    return;
                }
                let json_chunks = jsonize_stream_data(
                    stringify_stream_bytes(value)
                );
                update_chat(json_chunks);
                return reader.read().then(process);
            });
        })
        .catch((error) => console.error("Error:", error));
}

export var available_models = [];
export function request_available_models() {
    var url = "https://magic-api.ninomae.live/v1/models";
    let request_options = {
        method: "GET",
    };
    return fetch(url, request_options)
        .then((response) => response.json())
        .then((response_json) => {
            response_json.data.forEach((item) => {
                available_models.push(item.id);
            });
            available_models.sort();
            console.log(available_models);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}
