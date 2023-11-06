import { ChatCompletionsRequester } from "./llm_requester.js";
import { pop_messager } from "./chat_operator.js";

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
            if (event.key === "Enter" && !event.shiftKey && status !== "Stop") {
                event.preventDefault();
                await this.send(button);
            }
        });
    }
    async handle_user_input(button) {
        let user_input_content = $("#user-input").val();
        if (user_input_content === "") {
            return;
        }
        let status = button.text().trim();
        if (status === "Send") {
            this.send(button);
        } else if (status === "Regenerate") {
            this.regenerate(button);
        } else if (status === "Stop") {
            this.stop(button);
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

    async send(button) {
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
    }
    async regenerate(button) {
        console.log("Regenerate");
        button
            .text("Stop")
            .removeClass("btn-primary btn-success")
            .addClass("btn-warning");
        pop_messager(2);
        await this.post_user_input();
        button
            .text("Regenerate")
            .removeClass("btn-warning")
            .addClass("btn-success")
            .attr("disabled", false);
    }
    async stop(button) {
        console.log("Stop");
        this.requester.stop();
        button
            .attr("disabled", true)
            .removeClass("btn-warning")
            .addClass("btn-success")
            .text("Regenerate")
            .attr("disabled", false);
    }
    bind() {
        this.bind_send_user_input();
    }
}
