var source;

$("#send-user-input-btn").click(function () {
    var userInput = $("#userInput").val();
    // source = new EventSource("https://your-api-endpoint" + userInput);

    // source.onmessage = function (event) {
    //   $("#response").append("<p>" + event.data + "</p>");
    // };
    $(this).attr("disabled", true);
    $("#response").html("<p>" + userInput + "</p>");
    setTimeout(() => {
        $(this).attr("disabled", false);
        $(this).removeClass("btn-primary").addClass("btn-success");
    }, 1000);
    $(this).text("Regenerate");
});

$("#stop").click(function () {
    source.close();
});