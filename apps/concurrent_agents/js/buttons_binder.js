function bind_send_user_input() {
    $("#send-user-input").click(function () {
        let status = $(this).text().trim();
        if (status === "Stop") {
            console.log("Stop");
            $(this)
                .attr("disabled", true)
                .removeClass("btn-warning")
                .addClass("btn-success")
                .text("Regenerate")
                .attr("disabled", false);
            return;
        } else if (status === "Send" || status === "Regenerate") {
            console.log("Send");
            $(this).attr("disabled", true);
            $(this).removeClass("btn-success").addClass("btn-light");
            $(this)
                .text("Stop")
                .removeClass("btn-light")
                .addClass("btn-warning")
                .attr("disabled", false);
        } else {
            console.log("No action");
        }
    });
}

export function bind_buttons() {
    bind_send_user_input();
}
