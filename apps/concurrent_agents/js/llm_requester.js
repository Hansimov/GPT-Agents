import {
    jsonize_stream_data,
    stringify_stream_bytes,
} from "./stream_jsonizer.js";
import { openai_api_key } from "./secrets.js";

export function request_llm() {
    var url =
        "https://corsproxy.io/?https://magic-api.ninomae.live/v1/chat/completions";
    var request_options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${openai_api_key}`,
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [
                {
                    role: "user",
                    content:
                        "DO NOT SAY ANY OTHER THING. JUST REPEAT ONE WORD: 'hello'.",
                },
            ],
            temperature: 0,
            stream: true,
        }),
    };

    fetch(url, request_options)
        .then((response) => response.body)
        .then((rb) => {
            const reader = rb.getReader();
            return reader.read().then(function process({ done, value }) {
                if (done) {
                    return;
                }
                jsonize_stream_data(stringify_stream_bytes(value));
                return reader.read().then(process);
            });
        })
        .catch((error) => console.error("Error:", error));
}
