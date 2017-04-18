function error_message(message) {
    var submission_error = '<div class="alert alert-danger fade in" id="submission_error">' +
        '<a href="#" class="close" data-dismiss="alert">&times;</a>' +
        '<strong>Error!</strong> ' + message +
        '</div>';
     return submission_error
}

$("#addGroupButton").click(function() {
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
    $("#groupName").val("");
});

function deleteGroup(groupId) {
    $("#deleteGroupConfirmationModal").modal("show");
    $("#deleteGroupConfirmationButton").click(function() {
        var send = {"groupId": groupId};
        $.post("/deleteGroup/", send, function(data) {
            if(data["success"]) {
                location.reload();
            } else {
                $('.container').prepend(error_message(data["errorMessage"]));
            }
        });
        $("#deleteGroupConfirmationModal").modal("hide");
    });
}

function editGroup(groupId) {
    $("#editGroupModal").modal("show");
    $("#editGroupButton").click(function() {
        var groupName = $("#editedGroupName").val();
        var send = {"groupId": groupId, "groupName": groupName};
        $.post("/editGroup/", send, function(data) {
            if(data["success"]) {
                location.reload();
            } else {
                $('.container').prepend(error_message(data["errorMessage"]));
            }
        });
        $("#editGroupModal").modal("hide");
        $("#editedGroupName").val("");
    });
}
