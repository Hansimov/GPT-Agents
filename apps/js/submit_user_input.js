var source;

$("#send-user-input-btn").click(function () {
    var userInput = $("#userInput").val();
    var url = "https://magic-api.ninomae.live/v1/models";

    send_user_input_btn = $(this);

    $(this).attr("disabled", true);
    $(this).removeClass("btn-success").addClass("btn-light");
    available_models = $("#available-models");

    axios.get(url)
        .then(function (response) {
            console.log(response.data);
            var row = $('<div>').addClass('grid');
            response.data.data.forEach(function (item) {
                var col = $('<span>').addClass('available-model-item border p-1 m-0').append($('<span>').text(item.id));
                row.append(col);
            });

            available_models.html(row);

            send_user_input_btn.text("Regenerate");
            send_user_input_btn.removeClass("btn-light").addClass("btn-success");
            send_user_input_btn.attr("disabled", false);
        })
        .catch(function (error) {
            console.log(error);
        });

});
