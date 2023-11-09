import {
    setup_available_models_on_select,
    setup_temperature_on_select,
    setup_endpoint_and_key,
} from "./llm_models_loader.js";
import { bind_chat_buttons } from "./buttons_binder.js";
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

function setup_interactive_components() {
    setup_available_models_on_select();
    setup_temperature_on_select();
    auto_resize_user_input();
    bind_chat_buttons();
    register_user_input_history_buttons_callbacks();
    adjust_messagers_container_max_height();
    $(window).on("resize", adjust_messagers_container_max_height);
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

function adjust_messagers_container_max_height() {
    var user_interaction_height = $("#user-interactions").outerHeight(true);
    var page_height = $(window).height();
    $("#chat-session-container").css(
        "max-height",
        page_height - user_interaction_height - 30 + "px"
    );
}

$(document).ready(function () {
    setup_interactive_components();
});
