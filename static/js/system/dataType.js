function showAdd(that) {
    loadingOut();
    $(that).css('background-color', '#EB3C22').css('border-color', '#EB3C22');
    $(that).find('span').html('无法添加');
    setTimeout(function () {
        $(that).find('span').html('添加数据模板');
        $(that).css('background-color', '#57a2ff').css('border-color', '#57a2ff');
    }, 10000);
}