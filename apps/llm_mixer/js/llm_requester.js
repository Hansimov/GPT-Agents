import {
    jsonize_stream_data,
    stringify_stream_bytes,
} from "./stream_jsonizer.js";
import * as secrets from "./secrets.js";
import {
    update_message,
    create_messager,
    get_request_messages,
} from "./chat_operator.js";

export class ChatCompletionsRequester {
    constructor(
        prompt,
        model = "gpt-3.5-turbo",
        temperature = 0,
        messages = [],
        endpoint,
        cors_proxy
    ) {
        this.prompt = prompt;
        this.model = model;
        this.temperature = temperature;
        this.messages = messages;
        this.endpoint = endpoint || secrets.openai_endpoint;
        this.cors_proxy = cors_proxy || secrets.cors_proxy;
        this.request_endpoint = this.cors_proxy + this.endpoint;
        this.controller = new AbortController();
    }
    construct_request_messages() {
        this.request_messages = get_request_messages();
    }
    construct_request_headers() {
        this.request_headers = {
            "Content-Type": "application/json",
            Authorization: `Bearer ${secrets.openai_api_key}`,
        };
    }
    construct_request_body() {
        this.construct_request_messages();
        this.request_body = {
            model: this.model,
            messages: this.request_messages,
            temperature: this.temperature,
            stream: true,
        };
    }
    construct_request_params() {
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
        create_messager("user", this.prompt);
        create_messager("assistant", "", this.model, this.temperature);
        this.construct_request_params();
        return fetch(this.request_endpoint, this.request_params)
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
                    update_message(json_chunks);
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
