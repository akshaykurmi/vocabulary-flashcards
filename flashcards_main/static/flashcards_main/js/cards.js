function error_message(message) {
    var submission_error = '<div class="alert alert-danger fade in" id="submission_error">' +
        '<a href="#" class="close" data-dismiss="alert">&times;</a>' +
        '<strong>Error!</strong> ' + message +
        '</div>';
     return submission_error
}

$("#addCardButton").click(function() {
    var cardWord = $("#cardWord").val();
    var cardDefinition = $("#cardDefinition").val();
    var cardSentence = $("#cardSentence").val();
    var cardMnemonic = $("#cardMnemonic").val();
    console.log(cardWord)
    console.log(cardDefinition)
    console.log(cardSentence)
    console.log(cardMnemonic)
    var send = {"cardWord": cardWord,
                "cardDefinition": cardDefinition,
                "cardSentence": cardSentence,
                "cardMnemonic": cardMnemonic}
    $.post("addCard/", send, function(data) {
        if (data["success"]) {
            location.reload();
        } else {
            $('.container').prepend(error_message(data["errorMessage"]));
        }
    });
    $('#addCardModal').modal('hide');
    $("#cardWord").val("");
    $("#cardDefinition").val("");
    $("#cardSentence").val("");
    $("#cardMnemonic").val("");
});

function deleteCard(cardId) {
    $("#deleteCardConfirmationModal").modal("show");
    $("#deleteCardConfirmationButton").click(function() {
        var send = {"cardId": cardId};
        $.post("/deleteCard/", send, function(data) {
            if(data["success"]) {
                location.reload();
            } else {
                $('.container').prepend(error_message(data["errorMessage"]));
            }
        });
        $("#deleteCardConfirmationModal").modal("hide");
    });
}

function editCard(cardId) {
    $("#editCardModal").modal("show");
    $("#editCardButton").click(function() {
        var editedCardWord = $("#editedCardWord").val();
        var editedCardDefinition = $("#editedCardDefinition").val();
        var editedCardSentence = $("#editedCardSentence").val();
        var editedCardMnemonic = $("#editedCardMnemonic").val();
        var send = {"cardId": cardId,
                    "editedCardWord": editedCardWord,
                    "editedCardDefinition": editedCardDefinition,
                    "editedCardSentence": editedCardSentence,
                    "editedCardMnemonic": editedCardMnemonic}
        $.post("/editCard/", send, function(data) {
            if(data["success"]) {
                location.reload();
            } else {
                $('.container').prepend(error_message(data["errorMessage"]));
            }
        });
        $("#editCardModal").modal("hide");
        $("#editedCardWord").val("");
        $("#editedCardDefinition").val("");
        $("#editedCardSentence").val("");
        $("#editedCardMnemonic").val("");
    });
}