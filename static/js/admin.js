function adminList() {
    if (!$('.header .header-body .header-user .login-ul .h-u-h-c-b').hasClass('show')) {
        $('.header .header-body .header-user .login-ul .h-u-h-c-b').addClass('show');
    } else {
        $('.header .header-body .header-user .login-ul .h-u-h-c-b').removeClass('show');
    }
}

function reList() {
    $('.header .header-body .header-user .login-ul .h-u-h-c-b').removeClass('show')
}