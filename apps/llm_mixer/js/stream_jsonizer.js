const decoder = new TextDecoder("utf-8");

export function stringify_stream_bytes(bytes) {
    return decoder.decode(bytes);
}

export function jsonize_stream_data(data) {
    var json_chunks = [];
    data = data
        .replace(/^data:\s*/gm, "")
        .replace(/\[DONE\]/gm, "")
        .split("\n")
        .filter(function (line) {
            return line.trim().length > 0;
        })
        .map(function (line) {
            console.log(line);
            json_chunks.push(JSON.parse(line.trim()));
        });
    return json_chunks;
}

export function transform_footnote(text) {
    return text
        .replace(/\[\^(\d+)\^\]\[\d+\]/g, "[$1]")
        .replace(/\[(\d+)\]:\s*(.*)\s*""/g, "[$1] $2 \n");
}
