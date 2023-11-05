import { request_available_models, available_models } from "./llm_requester.js";

export async function setup_available_models_on_select() {
    var select = $("#available-models-select");
    select.empty();
    await request_available_models();
    var default_option = "gpt-3.5-turbo";

    $.each(available_models, function (index, value) {
        var option = new Option(value, index);
        select.append(option);
        if (value === default_option) {
            $(option).prop("selected", true);
        }
    });
}
