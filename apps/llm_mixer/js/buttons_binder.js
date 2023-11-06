import { ChatCompletionsRequester } from "./llm_requester.js";

export class ButtonsBinder {
    constructor() {
        this.requester = null;
    }
    bind_send_user_input() {
        const button = $("#send-user-input");
        button.click(async () => {
            await this.handle_user_input(button);
        });

        $("#user-input").keypress(async (event) => {
            let status = button.text().trim();
            if (
                event.key === "Enter" &&
                !event.shiftKey &&
                (status === "Send" || status === "Regenerate")
            ) {
                event.preventDefault();
                await this.handle_user_input(button);
            }
        });
    }
    async handle_user_input(button) {
        let status = button.text().trim();
        if (status === "Send" || status === "Regenerate") {
            console.log("Send");
            button
                .text("Stop")
                .removeClass("btn-primary btn-success")
                .addClass("btn-warning");
            await this.post_user_input();
            button
                .text("Regenerate")
                .removeClass("btn-warning")
                .addClass("btn-success")
                .attr("disabled", false);
        } else if (status === "Stop") {
            console.log("Stop");
            this.requester.stop();
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
    }
    async post_user_input() {
        let user_input_content = $("#user-input").val();
        console.log(user_input_content);
        this.requester = new ChatCompletionsRequester(user_input_content);
        await this.requester.post();
    }
    bind() {
        this.bind_send_user_input();
    }
}
