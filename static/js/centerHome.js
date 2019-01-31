function closechange(that) {
    loadingOut();
    $(that).parent().parent().css('display', 'none');
}

function changeUser_i(that) {
    loadingOut();
    $('#user-change').css('display', 'block');
    var change_id = $(that).parent().prev().attr('id');
    $('#user-change .change-table .change-table-form div form div .form-input #' + change_id).removeAttr('readonly').val('')
}

function changeUser_s(that) {
    loadingOut();
    $('#user-change').css('display', 'block');
    var change_id = $(that).parent().prev().attr('id');
    $('#user-change .change-table .change-table-form div form div .form-input #' + change_id).removeAttr('disabled')
}