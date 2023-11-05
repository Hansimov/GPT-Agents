export function create_chat_block(role = "assistant", content = "") {
    let chats_container = $("#chats-container");
    let chat_block = $("<div>").addClass(`chat-${role} mb-2 p-2`);
    chats_container.append(chat_block);
    chat_block.append(content);
    return chat_block;
}
export function get_latest_chat_block() {
    let chats_container = $("#chats-container");
    let chat_block = chats_container.children().last();
    return chat_block;
}

export function update_chat(json_chunks, chat_block = null) {
    if (chat_block === null) {
        chat_block = get_latest_chat_block();
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
        chat_block.append(content);
    });
    return json_chunks;
}
