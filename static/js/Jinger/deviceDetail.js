function mapGet(name, dict) {
    //获取数据
    var lostion = {"lat": dict['Lat'], "lon": dict['Lon']};
    var point = GpsToBaiduPoint(new BMap.Point(lostion.lon, lostion.lat));

    //第一个设备的位置作为地图初始化地点
    map.centerAndZoom(point, 19);

    //生成坐标对象
    var myIcon = new BMap.Icon("/static/img/jinger-maker.png", new BMap.Size(30, 30));
    Point = new BMap.Marker(point, {icon: myIcon});
    map.addOverlay(Point);
    //加入标签
    var label = new BMap.Label(name, {offset: new BMap.Size(36, -10)});
    Point.setLabel(label);
}

function mapGetWaring(name, dict) {
    //获取数据
    var lostion = {"lat": dict['Lat'], "lon": dict['Lon']};
    var point = GpsToBaiduPoint(new BMap.Point(lostion.lon, lostion.lat));

    //第一个设备的位置作为地图初始化地点
    map.centerAndZoom(point, 19);

    //生成坐标对象
    var myIcon = new BMap.Icon("/static/img/jinger-maker.png", new BMap.Size(30, 30));
    Point = new BMap.Marker(point, {icon: myIcon});
    map.addOverlay(Point);
    //加入标签
    var label = new BMap.Label(name, {offset: new BMap.Size(36, -10)});
    label.setStyle({
        color: '#EB3C22',
        border: 'none',
    });
    Point.setLabel(label);
}


function showremove(that) {
    loadingOut();
    $('#remove .grid .re-body div .id').html($(that).attr('did'));
    // 添加给删除界面
    $('#remove').attr('did', $(that).attr('did'));
    $('#remove').attr('dataid', $(that).attr('dataid'));
    $('#remove').css('display', 'block')
}

function reClose() {
    loadingOut();
    $('#remove').css('display', 'none')
}

function WaringRemove() {
    var did = $('#remove').attr('did');
    var dataid = $('#remove').attr('dataid');
    $.ajax({
        url: 'waringremove/',
        type: 'POST',
        data: {
            'dataid': dataid,
            'did': did,
            "csrfmiddlewaretoken": $("[name = 'csrfmiddlewaretoken']").val()
        },
        success: function (data) {
            if (data === '666') {
                loadingOut();
                window.location.reload()
            }
            else if (data === '444') {
                $('#remove .grid .re-body div').html('处理失败').css('color', 'red');
                setTimeout(function () {
                    window.location.reload();
                }, 1000);
            }
        }
    })
}

function mapGetNew() {
    $.ajax({
        url: 'getnewdevicemap/',
        type: 'POST',
        dataType: 'json',
        data: {
            "csrfmiddlewaretoken": $("[name = \'csrfmiddlewaretoken\']").val()
        },
        success: function (data) {
            if (data.status === 'waring') {
                map.removeOverlay(Point);
                mapGetWaring(data.name, data.data);
            }
            else {
                map.removeOverlay(Point);
                mapGet(data.name, data.data);
            }
        }
    })
}