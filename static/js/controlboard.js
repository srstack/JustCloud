// 查询是否存在异常
function getWaring() {
    $.ajax({
        url: '/getwaring/',
        type: 'GET',
        success: function (data) {
            if (data === 'yes') {
                $('#new_waring').css('display', 'block');
            }
            else {
                $('#new_waring').css('display', 'none');
            }
        }
    })
}

// 用户管理下拉框
function adminList() {
    if (!$('.header .header-body .header-user .login-ul .h-u-h-c-b').hasClass('show')) {
        $('.header .header-body .header-user .login-ul .h-u-h-c-b').addClass('show');
    } else {
        $('.header .header-body .header-user .login-ul .h-u-h-c-b').removeClass('show');
    }
}

// 关闭用户管理下拉框
function reList() {
    $('.header .header-body .header-user .login-ul .h-u-h-c-b').removeClass('show')
}

// 小飞机回到顶部
function showReposBtn() {
    var clientHeight = $(window).height() / 2;
    var scroll = $(document).scrollTop();
    if (scroll > clientHeight) {
        $('.suspension').show();
    } else {
        $('.suspension').hide();
    }
    ;
};
window.onload = function () {
    showReposBtn();
};
window.onscroll = function () {
    showReposBtn();
};

// 删除其余子元素的active类
function chosed(that) {
    that.firstElementChild.classList.add('active');
    $(that).parent().siblings().children('li').children('a.active').removeClass('active');
}

// 关闭警告页面
function waringClose() {
    loadingOut();
    $('#device_waring').css('display', 'none')
}


// 新警告事件刷新
function newWaring() {
    loadingOut();
    $('#new_waring').css('display', 'none')
}

function showmore(that) {
    now = $(that).attr('nowlen');
    len = $(that).attr('len');
    for (var i = 1; i < 6; i++) {
        var id = Number(now) + i;
        if (id === Number(len)) {
            $('#' + id).css('display', '');
            $(that).css('display', 'none');
            break
        }
        else {
            $('#' + id).css('display', '');
            $(that).attr('nowlen', id);
        }
    }
    loadingOut();
}
