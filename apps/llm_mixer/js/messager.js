export class MessagerViewer {
    constructor(message) {
        this.message = message;
        this.create_elements();
    }
    create_elements() {
        this.container = $("<div>").addClass("row no-gutters message-viewer");
        this.create_role_displayer();
        this.create_content_displayer();
        this.create_button();
        this.container
            .append(this.role_displayer)
            .append(this.content_displayer)
            .append(this.button);
    }
    create_role_displayer() {
        this.role_displayer = $("<div>")
            .addClass("col-auto mb-2 p-2")
            .addClass("role-displayer");
        if (this.message.role === "user") {
            this.role_displayer.append("You");
        } else {
            this.role_displayer.append(this.message.model);
        }
    }
    create_content_displayer() {
        this.content_displayer = $("<div>")
            .addClass("col mb-2 p-2")
            .addClass("content-displayer")
            .addClass(`chat-${this.message.role}`)
            .append(this.message.content);
    }
    create_button() {
        this.button = $("<button>").addClass(
            "col-auto btn btn-primary regenerate-button"
        );
        if (this.message.role === "user") {
            this.button.append("Edit");
        } else {
            this.button.append("Regenerate");
        }
    }
}

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
        let messager_viewer = new MessagerViewer(this.message);
        this.viewer = messager_viewer.container;
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
