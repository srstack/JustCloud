function get_error(that) {
    if (that.classList.contains('error')) {
        that.classList.remove('error');
        that.classList.add('waring');
        var label = that.nextSibling;
        that.value = '';
        that.setAttribute('placeholder', label.innerHTML)
    }
}

function createShow() {
    loadingOut();
    $('#create').css('display', 'block')
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

function showtype() {
    if ($('#platform').val() === 'Jinger') {
        $('#type').val('(\'Lon\',\'Lat\',\'Switch\',\'Cycle\',\'Turn\',)')
    }
    else if ($('#platform').val() === 'Detritus') {
        $('#type').val('（\'Lon\',\'Lat\',\'Switch\',\'Cycle\',\'Full\',)')
    }
    else if ($('#platform').val() === 'Lumiere') {
        $('#type').val('（\'Lon\',\'Lat\',\'Switch\',\'Cycle\',\'Switch-Light\',\'Top-Light\',\'Bottom-Light\',)')
    }
    else if ($('#platform').val() === 'Parquer') {
        $('#type').val('（\'Lon\',\'Lat\',\'Switch\',\'Cycle\',\'Park\',)')
    }
    else {
        $('#type').val('(\'\',)')
    }
}

function createSys() {
    var Status = true;
    var reg_value = $('#create .change-table .change-table-form > div > form').serializeArray();
    $.each(reg_value, function (i, val) {
        if (reg_value[i].value === "") {
            $('#create .change-table .change-table-form > div > form #' + reg_value[i].name).addClass('waring');
            Status = false;
        }
    });
    if (Status === true) {
        loadingIn();
        $.ajax({
            url: 'systemcreate/',
            type: 'POST',
            data: $('#create .change-table .change-table-form > div > form').serialize(),
            success: function (data) {
                if (data === '666') {
                    loadingOut();
                    $('#create').css('display', 'none');
                    $('.create-system').css('background-color', '#38B259').css('border-color', '#38B259');
                    $('.create-system>span').html('创建成功');
                    setTimeout(function () {
                        window.location.reload()
                    }, 3000);
                }
                else if (data === '222') {
                    loadingOut();
                    $('#create').css('display', 'none');
                    $('.create-system').css('background-color', '#EB3C22').css('border-color', '#EB3C22');
                    $('.create-system>span').html('模板格式错误');
                    setTimeout(function () {
                        $('.create-system>span').html('创建子系统');
                        $('.create-system').css('background-color', '#57a2ff').css('border-color', '#57a2ff');
                    }, 5000);
                }
                else if (data === '444') {
                    loadingOut();
                    $('#create').css('display', 'none');
                    $('.create-system').css('background-color', '#EB3C22').css('border-color', '#EB3C22');
                    $('.create-system>span').html('系统名已存在');
                    setTimeout(function () {
                        $('.create-system>span').html('创建子系统');
                        $('.create-system').css('background-color', '#57a2ff').css('border-color', '#57a2ff');
                    }, 5000);
                }
            }
        })
    }
}

