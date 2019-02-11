function showPush(that) {
    loadingOut();
    $('#push').attr('device_id', $(that).attr('did'));
    $('#push').css('display', 'block');
}

function showPushAll() {
    loadingOut();
    $('#pushall').css('display', 'block');
}

function closechange(that) {
    loadingOut();
    $(that).parent().parent().css('display', 'none');
    window.location.reload();
}

// 去除警告
function reWaring(that) {
    if (that.classList.contains('waring')) {
        that.classList.remove('waring');
        that.innerHTML = '';
    }
}

function dataPush() {
    loadingIn();
    var did = $('#push').attr('device_id');
    var data = $('#push .change-table .change-table-form div form').serialize();
    data = data + "&" + "did=" + did;
    $.ajax({
        url: 'pushadd/',
        type: 'POST',
        data: data,
        success: function (data) {
            if (data === '666') {
                loadingOut();
                $('#push').css('display', 'none');
                $('[did=' + did + ']').css('background-color', '#38B259').css('border-color', '#38B259');
                $('[did=' + did + ']').html('推送成功');
                loadingOut();
                setTimeout(function () {
                    window.location.reload();
                }, 3000);
            }
            else if (data === '444') {
                loadingOut();
                $('#push').css('display', 'none');
                $('[did=' + did + ']').css('background-color', '#EB3C22').css('border-color', '#EB3C22');
                $('[did=' + did + ']').find('span').html('无法推送');
                setTimeout(function () {
                    $('[did=' + did + ']').find('span').html('数据推送');
                    $('[did=' + did + ']').css('background-color', '#57a2ff').css('border-color', '#57a2ff');
                }, 10000);
            }
        }
    })
}

function dataPushAll() {
    loadingIn();
    var did = $('#pushall').attr('device_id');
    $.ajax({
        url: 'pushaddall/',
        type: 'POST',
        data: $('#pushall .change-table .change-table-form div form').serialize(),
        success: function (data) {
            if (data === '666') {
                loadingOut();
                $('#pushall').css('display', 'none');
                $('.push-add>a').css('background-color', '#38B259').css('border-color', '#38B259');
                $('.push-add>a>span').html('推送成功');
                loadingOut();
                setTimeout(function () {
                    window.location.reload();
                }, 3000);
            }
            else if (data === '444') {
                loadingOut();
                $('#pushall').css('display', 'none');
                $('.push-add>a').css('background-color', '#EB3C22').css('border-color', '#EB3C22');
                $('.push-add>a').find('span').html('无法推送');
                setTimeout(function () {
                    $('.push-add>a').find('span').html('数据推送');
                    $('.push-add>a').css('background-color', '#57a2ff').css('border-color', '#57a2ff');
                }, 10000);
            }
        }
    })
}