import { ChatCompletionsRequester } from "./llm_requester.js";
import { pop_messager } from "./chat_operator.js";

export class ButtonsBinder {
    constructor() {
        this.requester = null;
    }
    bind_send_user_input() {
        const button = $("#send-user-input");
        button.attr("status", "send");
        button.click(async () => {
            await this.handle_user_input(button);
        });

        $("#user-input").keypress(async (event) => {
            if (
                event.key === "Enter" &&
                !event.shiftKey &&
                button.attr("status") === "send"
            ) {
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
        let status = button.attr("status");
        if (status === "send") {
            this.send(button);
        } else if (status === "stop") {
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
        let button_icon = button.find("i");
        button.attr("status", "stop");
        button_icon
            .removeClass()
            .addClass("fa fa-circle-pause fa-fade")
            .css("color", "orange");
        await this.post_user_input();
        button.attr("status", "send");
        button_icon.removeClass().addClass("fa fa-paper-plane");
    }
    async stop(button) {
        console.log("Stop");
        let button_icon = button.find("i");
        this.requester.stop();
        button.attr("status", "send");
        button_icon
            .removeClass()
            .addClass("fa fa-paper-plane")
            .css("color", "red");
    }
    bind() {
        this.bind_send_user_input();
    }
}
