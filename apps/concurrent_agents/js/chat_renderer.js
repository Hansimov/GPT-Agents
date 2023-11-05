export function chat_renderer(json_chunks) {
    let chats_container = $("#chats-container");
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
        chats_container.append(content);
    });
    return json_chunks;
}
