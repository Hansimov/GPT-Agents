import { Messager, MessagerList } from "./messager.js";

let messagers_container = $("#messagers-container");
let messager_list = new MessagerList(messagers_container);

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
    messager_list.push(messager);
}

export function get_latest_message_viewer() {
    return messagers_container.children().last();
}
export function get_request_messages() {
    return messager_list.get_request_messages();
}

export function update_message(json_chunks, message_viewer = null) {
    if (message_viewer === null) {
        message_viewer = get_latest_message_viewer();
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
        }
        if (finish_reason === "stop") {
            console.log("[STOP]");
        }
        console.log(item);
        message_viewer.append(content);
    });
    return json_chunks;
}
