const decoder = new TextDecoder("utf-8");

export function stringify_stream_bytes(bytes) {
    return decoder.decode(bytes);
}

export function jsonize_stream_data(data) {
    var json_list = [];
    // iterate line by line, and convert each non-pure-whitespace line to json
    data = data
        .replace(/^data:\s*/gm, "")
        .split("\n")
        .filter(function (line) {
            return line.trim().length > 0;
        })
        .map(function (line) {
            json_list.push(JSON.parse(line.trim()));
        });

    // append the content to the text of the chats container
    var chats_container = $("#chats-container");
    json_list.forEach(function (item) {
        // chats_container.text = chats_container.text + item.choices[0].content;
        var choice = item.choices[0];
        var content = choice.delta.content;
        var role = choice.delta.role;
        var finish_reason = choice.finish_reason;
        if (role) {
            console.log("role: " + role);
        }
        if (content) {
            console.log(content);
        }
        if (finish_reason === "stop") {
            console.log("[STOP]");
        }
        chats_container.append(content);
    });
    return json_list;
}
