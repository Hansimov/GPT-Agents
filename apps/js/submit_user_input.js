var source;

$("#send-user-input").click(function () {
    var userInput = $("#sent-user-input").val();
    send_user_input_btn = $(this);
    $(this).attr("disabled", true);
    $(this).removeClass("btn-success").addClass("btn-light");
    $(this).text("Regenerate").removeClass("btn-light").addClass("btn-success").attr("disabled", false);

});

function load_available_models() {
    var url = "https://magic-api.ninomae.live/v1/models";
    available_models = $("#available-models");
    current_model = $("#current-model");
    axios.get(url)
        .then(function (response) {
            console.log(response.data);
            var row = $('<div>').addClass('grid');
            response.data.data.sort(function (a, b) {
                return a.id.localeCompare(b.id);
            }).forEach(function (item) {
                var col = $('<span>').addClass('available-model-item border p-1 m-0').append($('<span>').text(item.id));
                col.click(function () {
                    current_model.text(`Chat with: [${item.id}]`);
                    source = item.id;
                });
                row.append(col);
            });
            available_models.html(row);
        })
        .catch(function (error) {
            console.log(error);
        });
}

$(document).ready(function () {
    load_available_models();
});