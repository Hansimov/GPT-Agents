import { ChatCompletionsRequester } from "./llm_requester.js";

export class ButtonsBinder {
    constructor() {}
    bind_send_user_input() {
        const button = $("#send-user-input");
        button.click(async () => {
            let status = button.text().trim();
            if (status === "Send" || status === "Regenerate") {
                console.log("Send");
                button
                    .text("Stop")
                    .removeClass("btn-primary btn-success")
                    .addClass("btn-warning")
                    .attr("disabled", true);
                await this.post_user_input();
                button
                    .text("Regenerate")
                    .removeClass("btn-warning")
                    .addClass("btn-success")
                    .attr("disabled", false);
            } else if (status === "Stop") {
                console.log("Stop");
                button
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
    async post_user_input() {
        let user_input = $("#user-input").val();
        console.log(user_input);
        let requester = new ChatCompletionsRequester(user_input);
        await requester.post();
    }
    bind() {
        this.bind_send_user_input();
    }
}
