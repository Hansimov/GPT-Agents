import { setup_available_models_on_select } from "./llm_models_loader.js";
import { ButtonsBinder } from "./buttons_binder.js";
var user_input_history = [];
var user_input_history_idx = 0;

$("#user-input").on("enter", function () {
    console.log("enter");
});

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
    // request_llm();
    setup_available_models_on_select();
    let buttons_binder = new ButtonsBinder();
    buttons_binder.bind();

    // request_available_models();
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
    let prev_user_input = $("#prev-user-input");
    let next_user_input = $("#next-user-input");
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
