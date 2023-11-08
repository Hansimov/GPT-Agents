import { Messager, MessagerList } from "./messager.js";
import { transform_footnote } from "./stream_jsonizer.js";

let messagers_container = $("#messagers-container");
let available_models_select = $("#available-models-select");
let temperature_select = $("#temperature-select");

let messager_list = new MessagerList(messagers_container);
let chat_history = [messager_list];
let md_to_html_converter = new showdown.Converter();
md_to_html_converter.setFlavor("github");

export function get_active_messager_list() {
    return chat_history[chat_history.length - 1];
}

export function get_latest_messager() {
    return get_active_messager_list().messagers.slice(-1)[0];
}

export function create_messager(
    role,
    content = "",
    model = "",
    temperature = ""
) {
    let message = {
        role: role,
        content: content,
        model: model,
        temperature: temperature,
    };
    let messager = new Messager(message);
    get_active_messager_list().push(messager);
}

export function get_selected_llm_model() {
    return available_models_select.val();
}

export function get_selected_temperature() {
    return Number(temperature_select.val());
}

export function get_latest_messager_container() {
    return get_active_messager_list().messagers_container.children().last();
}
export function get_latest_message_content_displayer() {
    return get_latest_messager_container().find(".content-displayer");
}

export function get_latest_user_messager() {
    return $(".message-user").last();
}

export function start_latest_message_animation() {
    get_latest_messager_container()
        .find(".content-displayer")
        .addClass("blinking");
    get_latest_user_messager()
        .find(".button-group")
        .find(".regenerate-button")
        .find("i")
        .addClass("fa-spin-fast");
}

export function stop_latest_message_animation() {
    get_latest_messager_container()
        .find(".content-displayer")
        .removeClass("blinking");
    get_latest_user_messager()
        .find(".button-group")
        .find(".regenerate-button")
        .find("i")
        .removeClass("fa-spin-fast");
}

export function get_request_messages() {
    return get_active_messager_list().get_request_messages();
}

export function pop_messager(n = 2) {
    return get_active_messager_list().pop(n);
}

export function update_message(json_chunks, content_displayer = null) {
    if (content_displayer === null) {
        content_displayer = get_latest_message_content_displayer();
    }
    json_chunks.forEach(function (item) {
        let choice = item.choices[0];
        let content = choice.delta.content;
        let role = choice.delta.role;
        let finish_reason = choice.finish_reason;
        if (role) {
            console.log("role: " + role);
        }
        if (content) {
            console.log(content);
            content_displayer.data(
                "raw_content",
                content_displayer.data("raw_content") + content
            );
            get_active_messager_list().messagers.slice(-1)[0].message.content +=
                content;
            content_displayer.html(
                md_to_html_converter.makeHtml(
                    transform_footnote(content_displayer.data("raw_content"))
                )
            );
            content_displayer
                .find("table")
                .addClass("table table-bordered table-hover");
        }
        if (finish_reason === "stop") {
            console.log("[STOP]");
        }
        console.log(item);
    });
    return json_chunks;
}

export function create_new_chat_session() {
    let new_messager_list = new MessagerList(messagers_container);
    chat_history.push(new_messager_list);
    messagers_container.empty();
}
