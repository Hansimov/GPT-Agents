var source;

$("#send-user-input-btn").click(function () {
    var userInput = $("#userInput").val();
    var url = "https://ifconfig.me/ip";

    send_user_input_btn = $(this);

    $(this).attr("disabled", true);
    $(this).removeClass("btn-success").addClass("btn-light");

    axios.get(url)
        .then(function (response) {
            console.log(response.data);
            $("#response").html("<p>" + response.data + "</p>");
            send_user_input_btn.text("Regenerate");
            send_user_input_btn.removeClass("btn-light").addClass("btn-success");
            send_user_input_btn.attr("disabled", false);
        })
        .catch(function (error) {
            console.log(error);
        });

});
