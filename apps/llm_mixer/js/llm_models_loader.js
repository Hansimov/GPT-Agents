import { request_available_models, available_models } from "./llm_requester.js";

export async function setup_available_models_on_select(default_option = null) {
    var select = $("#available-models-select");
    select.empty();
    await request_available_models();
    if (default_option === null) {
        default_option = "gpt-3.5-turbo";
    }

    available_models.forEach((value, index) => {
        const option = new Option(value, value);
        select.append(option);
        if (value === default_option) {
            $(option).prop("selected", true);
        }
    });
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
