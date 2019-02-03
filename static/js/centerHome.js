// 关闭修改界面
function closechange(that) {
    loadingOut();
    $(that).parent().parent().css('display', 'none');
    window.location.reload();
}

// 不允许修改账号
function usernameChange(that) {
    loadingOut();
    $(that).css('background-color', '#EB3C22').css('border-color', '#EB3C22');
    $(that).find('span').html('账号无法修改');
    setTimeout(function () {
        $(that).find('span').html('修改账号');
        $(that).css('background-color', '#57a2ff').css('border-color', '#57a2ff');
    }, 10000);
}

// 显示修改密码界面
function passwordshow() {
    loadingOut();
    $('#password-change').css('display', 'block');
}

function changeUser_i(that) {
    loadingOut();
    $('#user-change').css('display', 'block');
    var change_id = $(that).parent().prev().attr('id');
    $('#user-change .change-table .change-table-form div form div .form-input #' + change_id).removeAttr('readonly').val('')
}

// 显示input框的用户信息修改
function changeUser_s(that) {
    loadingOut();
    $('#user-change').css('display', 'block');
    var change_id = $(that).parent().prev().attr('id');
    $('#user-change .change-table .change-table-form div form div .form-input #' + change_id).removeAttr('disabled')
}

// from表单验证
$().ready(function () {
    $('#user-change .change-table .change-table-form div form').validate({
        rules: {
            username: {
                required: true,
                minlength: 4
            },
            name: {
                required: true,
                maxlength: 20
            },
            phone: {
                required: true,
                digits: true,
                minlength: 11,
                maxlength: 11,
                number: true
            },
            email: {
                required: true,
                email: true
            },
            age : {
                digits: true,
                maxlength: 3
            }
        },
        messages: {
            username: {
                required: '用户账号不能为空！请输入！',
                minlength: '用户账号最少4位，请重新输入！'
            },
            name: {
                required: '用户名不能为空！请输入！',
                maxlength: '用户名最多20位，请重新输入！'
            },
            phone: {
                required: '用户手机号不能为空，请输入',
                digits: '手机号格式错误，请重新输入',
                minlength: '手机号格式错误，请重新输入',
                maxlength: '手机号格式错误，请重新输入',
                number: '手机号格式错误，请重新输入'
            },
            email: {
                required: '用户邮箱不能为空，请输入',
                email: '邮箱格式错误，请重新输入'
            },
            age: {
                digits: '年龄格式错误，请重新输入',
                maxlength: '年龄格式错误，请重新输入',
            }
        }
    })
});

// form表单验证（修改密码）
$().ready(function () {
    $('#password-change .change-table .change-table-form div form').validate({
        rules: {
            o_password: {
                required: true,
                minlength: 8
            },
            password: {
                required: true,
                minlength: 8
            },
            pwd_s: {
                required: true,
                minlength: 8,
                equalTo: "#password"
            },
        },
        messages: {
            o_password: {
                required: '旧密码不能为空，请输入',
                minlength: '旧密码长度不能小于8位，请重新输入',
            },
            password: {
                required: '新密码不能为空，请输入',
                minlength: '新密码长度不能小于8位，请重新输入',
            },
            pwd_s: {
                required: '请再次输入新密码',
                minlength: '新密码长度不能小于8位，请重新输入',
                equalTo: "两次密码需一致，请确认后再次输入"
            },
        }
    })
});

// 消除验证插件提示
function get_error(that) {
    if (that.classList.contains('error')) {
        that.classList.remove('error');
        that.classList.add('waring');
        var label = that.nextSibling;
        that.value = '';
        that.setAttribute('placeholder', label.innerHTML)
    }
}

// 去除警告
function reWaring(that) {
    if (that.classList.contains('waring')) {
        that.classList.remove('waring');
        that.innerHTML = '';
    }
}

// ajax 修改密码及回调函数
function passwordChange() {
    loadingOut();
    var Status = true;
    var reg_value = $('#password-change .change-table .change-table-form div form').serializeArray();
    $.each(reg_value, function (i, val) {
        if (reg_value[i].value === "") {
            $('#password-change .change-table .change-table-form div form #' + reg_value[i].name).addClass('waring');
            Status = false;
        }
    });
    if (Status === true) {
        loadingIn();
        $.ajax({
            url: 'passwordchange/',
            type: 'POST',
            data: $('#password-change .change-table .change-table-form div form').serialize(),
            success: function (data) {
                if (data === '666') {
                    $('#password-change').css('display', 'none');
                    $('.i-footer>button').css('background-color', '#38B259').css('border-color', '#38B259');
                    $('.i-footer>button>span').html('修改成功');
                    setTimeout(function () {
                        window.location.href = "/";
                    }, 3000);
                }
                else if (data === '777') {
                    loadingOut();
                    $('#password-change .change-table .change-table-form div form div div #o_password').addClass('waring').attr('placeholder', '旧密码错误').val('');
                }
            }
        })
    }
}

function userChange() {
    loadingOut();
    var Status = true;
    var reg_value = $('#user-change .change-table .change-table-form div form').serializeArray();
    $.each(reg_value, function (i, val) {
        if (reg_value[i].value === "") {
            if (reg_value[i].name === 'age' || reg_value[i].name === 'sex' ) {
                Status = true;
            }
            else {
                $('#user-change .change-table .change-table-form div form #' + reg_value[i].name).addClass('waring');
                Status = false;
            }
        }
    });
    if (Status === true) {
        loadingIn();
        $('#user-change .change-table .change-table-form div form div .form-input #sex').removeAttr('disabled');
        $.ajax({
            url: 'userchange/',
            type: 'POST',
            data: $('#user-change .change-table .change-table-form div form').serialize(),
            success: function (data) {
                if (data === '666') {
                    loadingOut();
                    window.location.reload();
                }
                else if (data === '777') {
                    loadingOut();
                    $('#user-change .change-table .change-table-form div form div div #phone').addClass('waring').attr('placeholder', '手机号已存在，请重新输入').val('');
                }
                else if (data === '888') {
                    loadingOut();
                    $('#user-change .change-table .change-table-form div form div div #email').addClass('waring').attr('placeholder', '邮箱存在，请重新输入').val('');
                }
            }
        })
    }
}