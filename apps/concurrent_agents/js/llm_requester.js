import {
    jsonize_stream_data,
    stringify_stream_bytes,
} from "./stream_jsonizer.js";
import { openai_api_key } from "./secrets.js";
import { chat_renderer } from "./chat_renderer.js";
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
            model: "bingo-precise",
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
                chat_renderer(json_chunks);
                return reader.read().then(process);
            });
        })
        .catch((error) => console.error("Error:", error));
}
