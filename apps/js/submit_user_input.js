var current_model;
var user_input_history = [];
var user_input_history_idx = 0;
var chat_models = [];

$("#user-input").on("enter", function () {
    console.log("enter");
});

$("#send-user-input").click(function () {
    $(this).attr("disabled", true);
    $(this).removeClass("btn-success").addClass("btn-light");
    $(this)
        .text("Regenerate")
        .removeClass("btn-light")
        .addClass("btn-success")
        .attr("disabled", false);
});

function load_available_models() {
    var url = "https://magic-api.ninomae.live/v1/models";
    available_models = $("#available-models");
    current_model = $("#current-model");
    axios
        .get(url)
        .then(function (response) {
            console.log(response.data);
            var row = $("<div>").addClass("grid");
            response.data.data
                .sort(function (a, b) {
                    return a.id.localeCompare(b.id);
                })
                .forEach(function (item) {
                    let model_id = item.id;
                    var col = $("<span>")
                        .addClass("available-model-item border p-1 m-0")
                        .append($("<span>").text(item.id));
                    col.click(function () {
                        if (chat_models.includes(item.id)) {
                            chat_models = chat_models.filter(function (
                                value,
                                index,
                                arr
                            ) {
                                return value !== item.id;
                            });
                            $(this).css("background-color", "");
                        } else {
                            chat_models.push(item.id);
                            $(this).css("background-color", "#d4edda");
                        }
                        current_model.text(chat_models);
                    });
                    col.attr("id", model_id);
                    row.append(col);
                });
            available_models.html(row);
        })
        .catch(function (error) {
            console.log(error);
        });
}

function auto_resize_user_input() {
    // https://stackoverflow.com/questions/37629860/automatically-resizing-textarea-in-bootstrap
    document.getElementById("user-input").addEventListener(
        "input",
        function () {
            this.style.height = 0;
            this.style.height = this.scrollHeight + 3 + "px";
        },
        false
    );
}

function register_user_input_callbacks() {
    // $("#user-input").on("keypress", function (event) {
    // if (event.key === "Enter" && !event.shiftKey) {

    // let current_user_input = $(this).val();
    // user_input_history.push(current_user_input);
    // $(this).val("");
    // user_input_history_idx = user_input_history.length;
    // set_user_input_history_buttons_state();
    // console.log(user_input_history);

    var url =
        "https://corsproxy.io/?https://magic-api.ninomae.live/v1/chat/completions";

    var request_options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${openai_api_key}`,
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [
                {
                    role: "user",
                    content: "Say hello to me.",
                },
            ],
            temperature: 0,
            stream: true,
        }),
    };
    fetch(url, request_options)
        .then((response) => response.body)
        .then((rb) => {
            const reader = rb.getReader();

            return new ReadableStream({
                start(controller) {
                    function push() {
                        reader.read().then(({ done, value }) => {
                            if (done) {
                                controller.close();
                                return;
                            }
                            controller.enqueue(value);
                            push();
                        });
                    }
                    push();
                },
            });
        })
        .then((stream) => {
            const reader = stream.getReader();
            const decoder = new TextDecoder("utf-8");
            var data = "";
            return reader.read().then(function process({ done, value }) {
                if (done) {
                    return data;
                }

                data = decoder.decode(value);
                data = data.replace(/^data:\s*/, "");
                data = JSON.stringify(data);
                // console.log(data);
                console.log(JSON.parse(data));
                return reader.read().then(process);
            });
    });

    // event.preventDefault();
    //     }
    // });
}

function register_user_input_history_buttons_callbacks() {
    set_user_input_history_buttons_state();
    $("#prev-user-input").click(function (event) {
        console.log("prev");
        user_input_history_idx = Math.max(0, user_input_history_idx - 1);
        user_input_history_value = user_input_history[user_input_history_idx];
        $("#user-input").val(user_input_history_value);
        set_user_input_history_buttons_state();
        event.preventDefault();
    });
    $("#next-user-input").click(function (event) {
        console.log("next");
        user_input_history_idx = Math.min(
            user_input_history.length - 1,
            user_input_history_idx + 1
        );
        user_input_history_value = user_input_history[user_input_history_idx];
        $("#user-input").val(user_input_history_value);
        set_user_input_history_buttons_state();
        event.preventDefault();
    });
}

function set_user_input_history_buttons_state() {
    prev_user_input = $("#prev-user-input");
    next_user_input = $("#next-user-input");
    if (user_input_history.length === 0) {
        prev_user_input.attr("disabled", true);
        next_user_input.attr("disabled", true);
    }
    if (user_input_history_idx >= user_input_history.length - 1) {
        next_user_input.attr("disabled", true);
    } else {
        next_user_input.attr("disabled", false);
    }

    if (user_input_history_idx <= 0) {
        prev_user_input.attr("disabled", true);
    } else {
        prev_user_input.attr("disabled", false);
    }
}

$(document).ready(function () {
    // load_available_models();
    auto_resize_user_input();
    register_user_input_callbacks();
    register_user_input_history_buttons_callbacks();
});
