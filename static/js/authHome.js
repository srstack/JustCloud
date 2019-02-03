// 展现删除界面
function showRemove(that) {
    loadingOut();
    $('#remove .grid .re-body div span').html($(that).prev().html());
    // 添加给删除界面
    $('#remove').attr('uid', $(that).attr('uid'));
    $('#remove').attr('sid', $(that).attr('sid'));
    $('#remove').css('display', 'block')
}

// 关闭页面
function reClose() {
    loadingOut();
    $('#remove').css('display', 'none')
}

// 删除管理权限
function adminRemove(that) {
    // 获得uid sid 通过showReomve获得
    var uid = $('#remove').attr('uid');
    var sid = $('#remove').attr('sid');
    $.ajax({
        url: 'adminremove/',
        type: 'POST',
        data: {
            'uid': uid,
            'sid': sid,
            "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()
        },
        success: function (data) {
            if (data === '666') {
                loadingOut();
                window.location.reload()
            }
            else if (data === '555') {
                $('#remove .grid .re-body div').html('无权限删除').css('color', 'red');
                setTimeout(function () {
                    window.location.reload();
                }, 1000);
            }
        }
    })
}

// 显示添加权限界面
function showAdd(that) {
    loadingOut();
    $('#sub_id').val($(that).attr('uid'));
    $('#sub_name').val($(that).attr('uname'));
    $('#sub_username').val($(that).attr('uuname'));
    $('#adminadd').css('display', 'block')
}

// 关闭添加权限界面
function closeadd() {
    loadingOut();
    $('#adminadd').css('display', 'none')
}

// Ajax添加权限
function adminAdd() {
    loadingIn();
    var u_id = $('#sub_id').val()
    $.ajax({
        url: 'adminadd/',
        type: 'POST',
        data: $('#adminadd .change-table .change-table-form div form').serialize(),
        success: function (data) {
            if (data === '666') {
                loadingOut();
                window.location.reload();
            }
            else if (data === '555') {
                loadingOut();
                $('#adminadd').css('display', 'none');
                $('#' + u_id + ' span').html('无权限操作');
                $('#' + u_id).css('background-color', '#EB3C22');
                setTimeout(function () {
                    $('#' + u_id + ' span').html('添加');
                    $('#' + u_id).css('background-color', '#57a2ff');
                }, 5000);
            }
            else if (data === '444') {
                loadingOut();
                $('#adminadd').css('display', 'none');
                $('#' + u_id + ' span').html('权限已存在');
                $('#' + u_id).css('background-color', '#EB3C22');
                setTimeout(function () {
                    $('#' + u_id + ' span').html('添加');
                    $('#' + u_id).css('background-color', '#57a2ff');
                }, 5000);
            }
        }
    })
}