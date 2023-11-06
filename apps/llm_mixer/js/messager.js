import { get_request_messages } from "./chat_operator.js";

export class Messager {
    constructor(message) {
        this.message = message;
        this.create_request_message();
        this.create_viewer();
    }
    create_request_message() {
        this.request_message = {
            role: this.message.role,
            content: this.message.content,
        };
    }
    create_viewer() {
        this.viewer = $("<div>").addClass(`chat-${this.message.role} mb-2 p-2`);
        this.viewer.append(this.message.content);
    }
}

export class MessagerList {
    constructor(messagers_container) {
        this.messagers_container = messagers_container;
        this.messagers = [];
    }

    push(messager) {
        this.messagers.push(messager);
        this.messagers_container.append(messager.viewer);
    }

    pop(n = 1) {
        let popped_messagers = this.messagers.splice(-n, n);
        this.messagers_container.children().slice(-n).remove();
        return popped_messagers;
    }

    extend(messagers) {
        this.messagers = this.messagers.concat(
            messagers.map(function (messager) {
                return messager;
            })
        );
        this.messagers_container.append(
            messagers.map(function (messager) {
                return messager.viewer;
            })
        );
    }

    clear() {
        this.messagers = [];
        this.messagers_container.empty();
    }

    get_messages() {
        return this.messagers.map(function (messager) {
            return messager.message;
        });
    }
    get_request_messages() {
        return this.messagers.map(function (messager) {
            return messager.request_message;
        });
    }

    get_message_viewers() {
        return this.messagers.map(function (messager) {
            return messager.viewer;
        });
    }
}
