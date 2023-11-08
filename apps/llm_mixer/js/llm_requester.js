import {
    jsonize_stream_data,
    stringify_stream_bytes,
} from "./stream_jsonizer.js";
// import * as secrets from "./secrets.js";
import {
    update_message,
    create_messager,
    get_request_messages,
    get_selected_llm_model,
    get_selected_temperature,
} from "./chat_operator.js";

export class ChatCompletionsRequester {
    constructor(
        prompt,
        model = null,
        temperature = null,
        endpoint = null,
        cors_proxy = null
    ) {
        this.prompt = prompt;
        this.model = model || get_selected_llm_model() || "gpt-turbo-3.5";
        this.temperature =
            temperature !== null ? temperature : get_selected_temperature();
        this.endpoint = endpoint || localStorage.getItem("openai_endpoint");
        this.cors_proxy = cors_proxy || "https://cors-anywhere.herokuapp.com/";
        this.request_endpoint = this.cors_proxy + this.endpoint;
        this.controller = new AbortController();
    }
    construct_request_messages() {
        this.request_messages = get_request_messages();
    }
    construct_request_headers() {
        this.request_headers = {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("openai_api_key")}`,
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
    create_messager_components() {
        create_messager("user", this.prompt);
        create_messager("assistant", "", this.model, this.temperature);
    }
    post() {
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
