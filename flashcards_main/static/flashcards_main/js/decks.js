function error_message(message) {
    var submission_error = '<div class="alert alert-danger fade in" id="submission_error">' +
        '<a href="#" class="close" data-dismiss="alert">&times;</a>' +
        '<strong>Error!</strong> ' + message +
        '</div>';
     return submission_error
}

$("#addDeckButton").click(function() {
    console.log("clicked");
    var deckName = $("#deckName").val();
    var send = {"deckName": deckName}
    $.post("addDeck/", send, function(data) {
        if (data["success"]) {
            location.reload();
        } else {
            $('.container').prepend(error_message(data["errorMessage"]));
        }
    });
    $('#addDeckModal').modal('hide');
    $("#deckName").val("");
});

function deleteDeck(deckId) {
    $("#deleteDeckConfirmationModal").modal("show");
    $("#deleteDeckConfirmationButton").click(function() {
        var send = {"deckId": deckId};
        $.post("/deleteDeck/", send, function(data) {
            if(data["success"]) {
                location.reload();
            } else {
                $('.container').prepend(error_message(data["errorMessage"]));
            }
        });
        $("#deleteDeckConfirmationModal").modal("hide");
    });
}

function editDeck(deckId) {
    $("#editDeckModal").modal("show");
    $("#editDeckButton").click(function() {
        var deckName = $("#editedDeckName").val();
        var send = {"deckId": deckId, "deckName": deckName};
        $.post("/editDeck/", send, function(data) {
            if(data["success"]) {
                location.reload();
            } else {
                $('.container').prepend(error_message(data["errorMessage"]));
            }
        });
        $("#editDeckModal").modal("hide");
        $("#editedDeckName").val("");
    });
}
