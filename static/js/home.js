function changeDoman() {
    loadingOut();
    if ($('.baseinfo .grid .baseinfo-user >span').html() === '管理员用户') {
       $('.change').css('display', 'block');
    }
    else {
        $('.domaninfo .grid .domaninfo-chenge>a>span').html('无权限操作');
        setTimeout(function () {
            $('.domaninfo .grid .domaninfo-chenge>a>span').html('修改所属域');
        }, 5000);
    }
}
function closeChange(that) {
    loadingOut();
    $(that).parent().parent().css('display','none')
}