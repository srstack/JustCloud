var i=0;
$(".wrapper-base .wrapper-index .w-banner .banner-sliders .num li").eq(0).addClass("active");
$(".wrapper-base .wrapper-index .w-banner .banner-sliders .num li").mouseover(function () {
    i = $(this).index();
    $(this).addClass("active").siblings().removeClass("active");
    $(".wrapper-base .wrapper-index .w-banner .banner-sliders .img li").eq(4-i).stop().fadeIn(1000).siblings().stop().fadeOut(200);
});
var c=setInterval(GO_R,5000);
function GO_R() {
    if (i == 4 - 1) {i = -1}
    i++;
    $(".wrapper-base .wrapper-index .w-banner .banner-sliders .num li").eq(i).addClass("active").siblings().removeClass("active");
    $(".wrapper-base .wrapper-index .w-banner .banner-sliders .img li").eq(i).stop().fadeIn(1000).siblings().stop().fadeOut(200)
}
$(".wrapper-base .wrapper-index .w-banner .banner-sliders").hover(function () {
    clearInterval(c)
},function () {
    c=setInterval(GO_R,5000)
});

function showReposBtn() {
    var clientHeight = $(window).height();
    var scrollTop = $(document).scrollTop();
    var maxScroll = $(document).height() - clientHeight;
    if (scrollTop > clientHeight) {
        $('.suspension').show();
    } else {
        $('.suspension').hide();
    };
};
window.onload = function() {
    showReposBtn();
};
window.onscroll = function () {
    showReposBtn();
};
function login() {
    var login_value = $('.modal-body form').serializeArray();
    $.each(login_value,function (i,val){
        if (login_value[i].value === "") {
            $('.modal-body form .form-group #' + login_value[i].name).addClass('waring');
            return false;
        }
    });
    $.ajax({
        url: 'login',
         type: 'POST',
         data: $(".modal-body form").serialize(),
         success: function (data) {
            if (data === 'success'){
                window.location.href="/keystone"
            }
         }
         })
}
function reWaring(that) {
    if (that.classList.contains('waring')){
        that.classList.remove('waring')
    }
};