import {
    jsonize_stream_data,
    stringify_stream_bytes,
} from "./stream_jsonizer.js";
import { openai_api_key } from "./secrets.js";
import { update_chat, create_chat_block } from "./chat_renderer.js";

export var chat_sessions = [];
export class ChatSession {
    constructor(messages = []) {
        this.messages = messages;
    }
    add_message(message) {
        this.messages.push(message);
    }
    pop_messages(n = 1) {
        return this.messages.splice(-n, n);
    }
    extend_messages(messages) {
        this.messages = this.messages.concat(messages);
    }
    clear() {
        this.messages = [];
    }
}

export class ChatCompletionsRequester {
    constructor(
        prompt,
        model = "gpt-3.5-turbo",
        temperature = 0,
        messages = [],
        endpoint = "https://corsproxy.io/?https://magic-api.ninomae.live/v1/chat/completions"
    ) {
        this.prompt = prompt;
        this.model = model;
        this.temperature = temperature;
        this.messages = messages;
        this.endpoint = endpoint;
        this.controller = new AbortController();
        this.construct_request_params();
    }
    construct_request_messages() {
        let message = {
            role: "user",
            content: this.prompt,
            model: this.model,
            temperature: this.temperature,
        };
        this.messages = this.messages.concat(message);
        this.request_messages = this.messages.map(({ role, content }) => ({
            role,
            content,
        }));
    }
    construct_request_headers() {
        this.request_headers = {
            "Content-Type": "application/json",
            Authorization: `Bearer ${openai_api_key}`,
        };
    }
    construct_request_body() {
        this.request_body = {
            model: this.model,
            messages: this.request_messages,
            temperature: this.temperature,
            stream: true,
        };
    }
    construct_request_params() {
        this.construct_request_messages();
        this.construct_request_headers();
        this.construct_request_body();
        this.request_params = {
            method: "POST",
            headers: this.request_headers,
            body: JSON.stringify(this.request_body),
            signal: this.controller.signal,
        };
    }
    post() {
        create_chat_block("user", this.prompt);
        create_chat_block("assistant");
        return fetch(this.endpoint, this.request_params)
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
    stop() {
        this.controller.abort();
    }
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
