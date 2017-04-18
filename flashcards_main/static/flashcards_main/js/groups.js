function error_message(message) {
    var submission_error = '<div class="alert alert-danger fade in" id="submission_error">' +
        '<a href="#" class="close" data-dismiss="alert">&times;</a>' +
        '<strong>Error!</strong> ' + message +
        '</div>';
     return submission_error
}

$("#addGroupButton").click(function() {
    console.log("clicked");
    var groupName = $("#groupName").val();
    var send = {"groupName": groupName}
    $.post("/addGroup/", send, function(data) {
        if (data["success"]) {
            location.reload();
        } else {
            $('.container').prepend(error_message(data["errorMessage"]));
        }
    });
    $('#addGroupModal').modal('hide');
    $("#groupName").val("")
});