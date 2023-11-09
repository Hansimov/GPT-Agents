import { request_available_models, available_models } from "./llm_requester.js";

export async function setup_available_models_on_select(default_option = null) {
    var select = $("#available-models-select");
    select.empty();
    await request_available_models();
    const working_models = [
        "bing-precise",
        "bing-balanced",
        "bing-creative",
        // "bing-dall-e", // not work
        "bing-gpt-4",
        "bing-gpt-4-32k",
        // "bingo-balanced", // not work
        // "bingo-creative", // not work
        // "bingo-precise", // not work
        "claude-2",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-internet",
        "gpt-4",
        "gpt-4-32k",
        "gpt-4-internet",
        // "pandora-gpt-3.5-turbo", // not work
        // "poe-claude-2-100k", // not work
        "poe-claude-instant",
        "poe-claude-instant-100k",
        // "poe-code-llama-13b",
        // "poe-code-llama-34b",
        // "poe-code-llama-7b",
        // "poe-dolly-v2-12b", // not work
        "poe-google-palm",
        "poe-gpt-3.5-turbo",
        // "poe-gpt-3.5-turbo-16k", // not work
        "poe-gpt-3.5-turbo-instruct",
        "poe-gpt-4",
        "poe-gpt-4-32k",
        // "poe-llama-2-13b",
        // "poe-llama-2-70b",
        // "poe-llama-2-7b",
        // "poe-nous-hermes-13b",
        // "poe-nous-hermes-l2-13b", // not work
        // "poe-saga",
        // "poe-solar-0-70b",
        // "poe-stablediffusion-xl", // not work
        // "poe-starcoderchat", // not work
        "poe-web-search",
    ];
    working_models.forEach((value, index) => {
        const option = new Option(value, value);
        if (available_models.includes(value)) {
            select.append(option);
        }
    });
    let default_model = "gpt-turbo-3.5";
    if (localStorage.getItem("default_model")) {
        default_model = localStorage.getItem("default_model");
    }
    select.val(default_model);
    console.log(`Default model: ${select.val()}`);
}

export async function setup_temperature_on_select(default_option = null) {
    var select = $("#temperature-select");
    select.empty();
    if (default_option === null) {
        default_option = "0";
    }
    for (let i = 10; i >= 0; i--) {
        const value = i / 10;
        const option = new Option(value, value);
        select.append(option);
        if (value === Number(default_option)) {
            $(option).prop("selected", true);
        }
    }
    console.log(`Default temperature: ${select.val()}`);
}

export function setup_endpoint_and_key() {
    if (localStorage.getItem("openai_endpoint")) {
        $("#openai-endpoint").val(localStorage.getItem("openai_endpoint"));
        console.log("GET: OpenAI Endpoint!");
    } else {
        console.log("NULL: OpenAI Endpoint!");
        $("#openai-endpoint").on("submit", function (event) {
            event.preventDefault();
            localStorage.setItem(
                "openai_endpoint",
                $("#openai-endpoint").val()
            );
            console.log("SET: OpenAI Endpoint!");
        });
    }

    if (localStorage.getItem("openai_api_key")) {
        $("#openai-api-key").val(localStorage.getItem("openai_api_key"));
        console.log("GET: OpenAI API Key!");
    } else {
        console.log("NULL: OpenAI API Key!");
        $("#openai-api-key").on("submit", function (event) {
            event.preventDefault();
            localStorage.setItem("openai_api_key", $("#openai-api-key").val());
            console.log("SET: OpenAI API Key!");
        });
    }
}
