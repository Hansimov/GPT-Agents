import { ChatCompletionsRequester } from "./llm_requester.js";
function bind_send_user_input() {
    $("#send-user-input").click(function () {
        let status = $(this).text().trim();
        if (status === "Send" || status === "Regenerate") {
            console.log("Send");
            $(this)
                .text("Stop")
                .removeClass("btn-primary")
                .removeClass("btn-success")
                .addClass("btn-warning")
                .attr("disabled", true);
            post_user_input();
            $(this)
                .text(status)
                .removeClass("btn-warning")
                .addClass("btn-success")
                .attr("disabled", false);
        } else if (status === "Stop") {
            console.log("Stop");
            $(this)
                .attr("disabled", true)
                .removeClass("btn-warning")
                .addClass("btn-success")
                .text("Regenerate")
                .attr("disabled", false);
            return;
        } else {
            console.log("No action");
        }
    });
}
async function post_user_input() {
    let user_input = $("#user-input").val();
    console.log(user_input);
    let requester = new ChatCompletionsRequester(user_input);
    await requester.post();
}

export function bind_buttons() {
    bind_send_user_input();
}
