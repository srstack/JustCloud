function getDay(day) {
    var today = new Date();
    var targetday_milliseconds = today.getTime() + 1000 * 60 * 60 * 24 * day;
    today.setTime(targetday_milliseconds); //注意，这行是关键代码
    var tYear = today.getFullYear();
    var tMonth = today.getMonth();
    var tDate = today.getDate();
    tMonth = doHandleMonth(tMonth + 1);
    tDate = doHandleMonth(tDate);
    return tYear + "-" + tMonth + "-" + tDate;
}

function doHandleMonth(month) {
    var m = month;
    if (month.toString().length == 1) {
        m = "0" + month;
    }
    return m;
}

function showremove(that) {
    loadingOut();
    $('#remove .grid .re-body div .id').html($(that).attr('did'));
    // 添加给删除界面
    $('#remove').attr('did', $(that).attr('did'));
    $('#remove').css('display', 'block')
}

function reClose() {
    loadingOut();
    $('#remove').css('display', 'none')
}

function deviceRemove() {
    var did = $('#remove').attr('did');
    loadingIn();
    $.ajax({
        url: 'deviceremove/',
        type: 'POST',
        data: {
            'did': did,
            "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()
        },
        success: function (data) {
            if (data === '666') {
                loadingOut();
                window.location.reload()
            }
            else if (data === '444') {
                $('#remove .grid .re-body div').html('无权限删除').css('color', 'red');
                setTimeout(function () {
                    window.location.reload();
                }, 1000);
            }
        }
    })
}

function createShow() {
    loadingOut();
    $('#deviceadd').css('display', 'block')
}

function closeChange(that) {
    loadingOut();
    $(that).parent().parent().css('display', 'none')
}

function reWaring(that) {
    if (that.classList.contains('waring')) {
        that.classList.remove('waring');
        that.innerHTML = '';
    }
}

function get_error(that) {
    if (that.classList.contains('error')) {
        that.classList.remove('error');
        that.classList.add('waring');
        var label = that.nextSibling;
        that.value = '';
        that.setAttribute('placeholder', label.innerHTML)
    }
}

// ajax创建系统
function createSys() {
    var Status = true;
    var reg_value = $('#deviceadd .change-table .change-table-form > div > form').serializeArray();
    $.each(reg_value, function (i, val) {
        if (reg_value[i].value === "") {
            $('#deviceadd .change-table .change-table-form > div > form #' + reg_value[i].name).addClass('waring');
            Status = false;
        }
    });
    if (Status === true) {
        loadingIn();
        $.ajax({
            url: 'deviceadd/',
            type: 'POST',
            data: $('#deviceadd .change-table .change-table-form > div > form').serialize(),
            success: function (data) {
                if (data === '666') {
                    $('#deviceadd').css('display', 'none');
                    $('.create-device').css('background-color', '#38B259').css('border-color', '#38B259');
                    $('.create-device>span').html('创建成功');
                    setTimeout(function () {
                        window.location.reload()
                    }, 2000);
                }
                else if (data === '444') {
                    loadingOut();
                    $('#deviceadd').css('display', 'none');
                    $('.create-device').css('background-color', '#EB3C22').css('border-color', '#EB3C22');
                    $('.create-device>span').html('设备名已存在');
                    setTimeout(function () {
                        $('.create-device>span').html('添加设备');
                        $('.create-device').css('background-color', '#57a2ff').css('border-color', '#57a2ff');
                    }, 5000);
                }
            }
        })
    }
}

// form表单验证
$().ready(function () {
    $('#deviceadd .change-table .change-table-form div form').validate({
        rules: {
            IMEI: {
                required: true,
                minlength: 15,
                maxlength: 15,
                digits: true,
                number: true

            },
        },
        messages: {
            IMEI: {
                required: '请输入IMEI序列号',
                minlength: 'IMEI长度不能小于15位，请重新输入',
                maxlength: 'IMEI长度不能大于15位，请重新输入',
                digits: 'IMEI格式错误，请重新输入',
                number: 'IMEI格式错误，请重新输入',
            },
        }
    })
});