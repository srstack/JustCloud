var i = 0;
$(".wrapper-base .wrapper-index .w-banner .banner-sliders .num li").eq(0).addClass("active");
$(".wrapper-base .wrapper-index .w-banner .banner-sliders .num li").mouseover(function () {
    i = $(this).index();
    $(this).addClass("active").siblings().removeClass("active");
    $(".wrapper-base .wrapper-index .w-banner .banner-sliders .img li").eq(4 - i).stop().fadeIn(1000).siblings().stop().fadeOut(200);
});
var c = setInterval(GO_R, 5000);

function GO_R() {
    if (i == 4 - 1) {
        i = -1
    }
    i++;
    $(".wrapper-base .wrapper-index .w-banner .banner-sliders .num li").eq(i).addClass("active").siblings().removeClass("active");
    $(".wrapper-base .wrapper-index .w-banner .banner-sliders .img li").eq(i).stop().fadeIn(1000).siblings().stop().fadeOut(200)
}

$(".wrapper-base .wrapper-index .w-banner .banner-sliders").hover(function () {
    clearInterval(c)
}, function () {
    c = setInterval(GO_R, 5000)
});

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

function login() {
    var to_hanzi = {'domain': '域名', 'username': '用户名', 'password': '密码'}
    var Status = true;
    var login_value = $('.modal-body form').serializeArray();
    $.each(login_value, function (i, val) {
        if (login_value[i].value === "") {
            $('.modal-body form .form-group #' + login_value[i].name).addClass('waring').attr('placeholder', to_hanzi[login_value[i].name] + '不能为空，请输入');
            Status = false;
        }
    });
    if (Status === true) {
        loadingIn()
        $.ajax({
            url: '/login/',
            type: 'POST',
            data: $(".modal-body form").serialize(),
            success: function (data) {
                if (data === '666') {
                    loadingOut()
                    window.location.href = "/"
                }
                else if (data === '555') {
                    loadingOut()
                    $('.modal-body form .form-group #password').addClass('waring').attr('placeholder', '密码错误，请重新输入').val('');
                }
                else if (data === '444') {
                    loadingOut()
                    $('.modal-body form .form-group #username').addClass('waring').attr('placeholder', '用户名错误或不存在，请重新输入').val('');
                }
                else if (data === '333') {
                    loadingOut()
                    $('.modal-body form .form-group #domain').addClass('waring').attr('placeholder', '域名错误或不存在，请重新输入').val('');
                }
            }
        })
    }
}

function reWaring(that) {
    if (that.classList.contains('waring')) {
        that.classList.remove('waring');
    }
}

function adminList() {
    if ($('.header .header-body .header-user .login-ul .h-u-h-c-b').hasClass('hide')){
        $('.header .header-body .header-user .login-ul .h-u-h-c-b').addClass('show').removeClass('hide');
    }
    else {
        $('.header .header-body .header-user .login-ul .h-u-h-c-b').addClass('hide').removeClass('show');
    }
}
function reList() {
    $('.header .header-body .header-user .login-ul .h-u-h-c-b').addClass('hide').removeClass('show')
}