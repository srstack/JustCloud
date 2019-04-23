from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
from django.db.models import F, Q
import datetime, time
import json


def waringDevice(user_obj):
    devices = []
    system = []
    waring_devices = []
    for system_obj in user_obj.system.all():
        for device_obj in system_obj.device.all():
            devices.append(device_obj)
    for device_obj in devices:
        if device_obj.data.filter(waring=1):
            system.append(device_obj.system)
            waring_devices.append(device_obj)
    return system, waring_devices


# Create your views here.

def systemMain(request, username, sid):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            main_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '系统概况'

            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                # 设备queryset
                devices = system_obj.device.all()
                device_count = len(devices)

                # 在线设备/不在线设备
                device_active_list = []
                device_inactive_list = []
                # 数据信息
                data_count = 0
                push_count = 0
                pull_count = 0
                new_data_count = 0
                # 今日时间
                now_time = datetime.datetime.now()
                now_day = now_time.date()
                # 运行天数
                running_days = (now_day - system_obj.date.date()).days
                # 最近五天
                time_list = [now_day, ]
                tmp_time = now_day
                yes_time = datetime.timedelta(days=-1)
                for i in range(0, 4):
                    time_list.append(tmp_time + yes_time)
                    tmp_time = tmp_time + yes_time
                time_list.reverse()

                data_push_list = [0, 0, 0, 0, 0]
                data_pull_list = [0, 0, 0, 0, 0]
                data_waring_list = [0, 0, 0, 0, 0]

                new_devices = []
                # 该系统的异常设备
                system_waring_devices = []
                for device in devices:
                    if device.data.all():
                        device_active_list.append(device)
                    else:
                        device_inactive_list.append(device)
                    if device.date.date() == now_day:
                        new_devices.append(device)
                    data_count = data_count + len(device.data.all())
                    data_list = device.data.filter(date__gte=now_time)
                    for data in data_list:
                        if data.waring == 1 and data.model == 0:
                            system_waring_devices.append(device)
                        if data.model:
                            push_count = push_count + 1
                        else:
                            pull_count = pull_count + 1
                        if data.date.date() == now_day:
                            new_data_count = new_data_count + 1
                        for i in range(0, 5):
                            if data.date.date() == time_list[i]:
                                if data.model:
                                    data_push_list[i] = data_push_list[i] + 1
                                else:
                                    # 订阅数据中的异常数据
                                    if data.waring == 0 or data.waring == 1:
                                        data_waring_list[i] = data_waring_list[i] + 1
                                    # 正常数据
                                    else:
                                        data_pull_list[i] = data_pull_list[i] + 1

                # 利用集合的特性去重
                system_waring_devices = list(set(system_waring_devices))
                system_waring_device_count = len(system_waring_devices)

                data_waring_count = len(data_waring_list)
                device_active_count = len(device_active_list)
                device_inactive_count = len(device_inactive_list)
                new_devices_count = len(new_devices)
                new_device_active = 0
                new_device_inactive = 0
                for device in new_devices:
                    if device in device_active_list:
                        if not (device in system_waring_devices):
                            new_device_active = new_device_active + 1
                    else:
                        new_device_inactive = new_device_inactive + 1

                return render(request, 'system/systemMain.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def systemAnaly(request, username, sid):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            analy_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '系统分析'
            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限

            if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                # 设备queryset
                devices = system_obj.device.all()
                device_count = len(devices)

                if not system_obj.device.filter(data__model=0):
                    return render(request,'system/noDataAnaly.html',locals())

                # 该系统的异常设备
                system_waring_devices = []
                system_waring_datas = []
                for device in devices:
                    for data in device.data.filter(model=0).all():
                        if data.waring == 1:
                            system_waring_devices.append(device)
                            system_waring_datas.append(data)

                # 利用集合的特性去重
                system_waring_devices = list(set(system_waring_devices))
                system_waring_device_count = len(system_waring_devices)
                system_waring_data_count = len(system_waring_datas)

                # 数据模板
                type_name = eval(str(system_obj.type))
                data_type = type_name.keys()
                data_type_count = len(data_type)

                device_map = {}
                waring_device_map = {}

                # 活跃设备，非在线设备
                active_count = 0

                full_map = {}

                # 地图数据
                for device in devices:
                    if device.data.filter(model=0).all() and device not in system_waring_devices:
                        active_count += 1
                        data = eval(str(device.data.filter(model=0).last()))
                        device_map[device.name] = {}
                        full_map[device.name] = []
                        for key_data, value_data in data.items():
                            if key_data in data_type:
                                device_map[device.name][key_data] = value_data
                        for data in device.data.filter(model=0).all():
                            if eval(str(data.data))['Full'] == 1:
                                date_list = [int(time.mktime(data.date.date().timetuple())) * 1000,
                                             (int(time.mktime(data.date.timetuple())) - int(
                                                 time.mktime(data.date.date().timetuple())) - (8 * 3600)) * 1000
                                             ]
                                full_map[device.name].append(date_list)

                # 异常设备地图数据
                for device in system_waring_devices:
                    data = eval(str(device.data.filter(model=0).last()))
                    waring_device_map[device.name] = {}
                    full_map[device.name] = []
                    for key_data, value_data in data.items():
                        if key_data in data_type:
                            waring_device_map[device.name][key_data] = value_data
                    for data in device.data.filter(model=0).all():
                        if eval(str(data.data))['Full'] == 1:
                            date_list = [int(time.mktime(data.date.date().timetuple())) * 1000,
                                         (int(time.mktime(data.date.timetuple())) - int(
                                             time.mktime(data.date.date().timetuple())) - (8 * 3600)) * 1000]
                            full_map[device.name].append(date_list)

                return render(request, 'detritus/detritusAnaly.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def systemDevice(request, username, sid):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            device_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '设备列表'

            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':
                # 设备queryset
                devices = system_obj.device.all()
                device_count = len(devices)

                # 在线设备/不在线设备
                device_active_list = []
                device_inactive_list = []

                # 今日时间
                now_time = datetime.datetime.now()
                now_day = now_time.date()

                # 最近十天
                time_list = [now_day, ]
                tmp_time = now_day
                yes_time = datetime.timedelta(days=-1)
                for i in range(0, 9):
                    time_list.append(tmp_time + yes_time)
                    tmp_time = tmp_time + yes_time
                time_list.reverse()

                device_new_change_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                device_waring_change_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                device_count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                new_devices = []
                # 该系统的异常设备

                system_waring_devices = []
                for device in devices:
                    data_list = []
                    if device.data.all():
                        device_active_list.append(device)
                    else:
                        device_inactive_list.append(device)
                    if device.date.date() == now_time:
                        new_devices.append(device)
                    if Data.objects.filter(model=0, date__gte=time_list[0], device=device):
                        system_waring_devices.append(device)
                    data_list = Data.objects.filter(Q(waring=1) | Q(waring=0), model=0, date__gte=time_list[0],
                                                    device=device)
                    print(data_list)
                    for i in range(0, 10):
                        if device.date.date() == time_list[i]:
                            device_new_change_list[i] = device_new_change_list[i] + 1
                        if device.date.date() <= time_list[i]:
                            device_count_list[i] = device_count_list[i] + 1
                        if data_list:
                            for data in data_list:
                                if data.date.date() == time_list[i]:
                                    device_waring_change_list[i] = device_waring_change_list[i] + 1
                                    print(device_waring_change_list)
                                    break

                # 利用集合的特性去重
                system_waring_devices = list(set(system_waring_devices))
                system_waring_device_count = len(system_waring_devices)

                device_active_count = len(device_active_list)
                device_inactive_count = len(device_inactive_list)
                new_devices_count = len(new_devices)
                return render(request, 'system/systemDevice.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def deviceDetail(request, username, sid, did):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            device_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '设备详情'
            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 设备对象
            device_obj = Device.objects.filter(id=did)
            if device_obj:
                device_obj = device_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限

            if device_obj.system == system_obj:
                pass
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            if user_obj in device_obj.system.admin.all() and system_obj.platform == 'Detritus':

                # 数据模板
                type_name = eval(str(system_obj.type))
                data_type = type_name.keys()

                device_map = {}

                # 地图数据
                data = eval(str(device_obj.data.filter(model=0).all().last()))

                if data:
                    pass
                else:
                    return render(request, 'system/noDataDetail.html', locals())

                for key_data, value_data in data.items():
                    if key_data in data_type:
                        device_map[key_data] = value_data

                if device_obj.data.filter(waring=1, model=0):
                    waring_data = device_obj.data.filter(waring=1, model=0).last()
                    waring_device_map = True

                data_had_waring = device_obj.data.filter(Q(waring=1, model=0) | Q(waring=0, model=0)).order_by('-id')
                data_had_waring_count = len(data_had_waring)

                # 历史异常数据
                data_waring_dict = {}
                for data in data_had_waring:
                    data_waring_dict[data.id] = eval(str(data.data))

                return render(request, 'system/deviceDetail.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def dataType(request, username, sid):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            type_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '数据模板'

            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                # 数据模板
                type_name = eval(str(system_obj.type))
                data_type = type_name.keys()
                data_type_count = len(data_type)

                return render(request, 'system/dataType.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def systemPush(request, username, sid):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            push_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '命令推送'

            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                # 设备queryset
                devices = system_obj.device.all()

                # 数据模板
                type_name = eval(str(system_obj.type))
                data_type = type_name.keys()

                device_data_dict = {}
                data_dict = {}

                push_count = 0

                # 推送数据
                for device in devices:
                    data_list = device.data.filter(model=1).all()
                    device_data_dict[device] = []
                    push_count = push_count + len(data_list)
                    if data_list:
                        for data in data_list:
                            device_data_dict[device].insert(0, data)
                            data_dict[data.id] = eval(str(data.data))

                return render(request, 'system/systemPush.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def systemPull(request, username, sid):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 拿到用户ORM对象
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            pull_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '数据订阅'

            # 系统对象
            system_obj = System.objects.filter(id=sid)
            if system_obj:
                system_obj = system_obj[0]
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))

            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                # 设备queryset
                devices = system_obj.device.all()

                # 数据模板
                type_name = eval(str(system_obj.type))
                data_type = type_name.keys()

                device_data_dict = {}
                data_dict = {}

                pull_count = 0

                # 订阅数据
                for device in devices:
                    data_list = device.data.filter(model=0).all()
                    device_data_dict[device] = []
                    pull_count = pull_count + len(data_list)
                    if data_list:
                        for data in data_list:
                            device_data_dict[device].insert(0, data)
                            data_dict[data.id] = eval(str(data.data))

                return render(request, 'system/systemPull.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def waringRemove(request, username, sid, did=0):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                # 系统对象
                system_obj = System.objects.filter(id=sid)
                if system_obj:
                    system_obj = system_obj[0]
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]

                # 判断是否有管理权限
                if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                    # 获得post数据
                    device_id = request.POST.get('did')
                    data_id = request.POST.get('dataid')

                    data_obj = Data.objects.filter(id=data_id, device_id=device_id, waring=1)
                    if data_obj:
                        data_obj = data_obj[0]
                        data_obj.waring = 0
                        data_obj.save()
                        # 操作记录
                        Operation.objects.create(code=401, user=user_obj)
                        return HttpResponse('666')
                    else:
                        return HttpResponse('444')
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def deviceRemove(request, username, sid):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                # 系统对象
                system_obj = System.objects.filter(id=sid)
                if system_obj:
                    system_obj = system_obj[0]
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]

                # 判断是否有管理权限
                if user_obj in system_obj.admin.all() and system_obj.platform == 'Detritus':

                    # 获得post数据
                    device_id = request.POST.get('did')

                    device_obj = Device.objects.filter(id=device_id, system_id=sid)
                    if device_obj:
                        data_obj = device_obj[0]
                        data_obj.delete()
                        # 操作记录
                        Operation.objects.create(code=303, user=user_obj)
                        return HttpResponse('666')
                    else:
                        return HttpResponse('444')
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def deviceAdd(request, username, sid):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                # 系统对象
                system_obj = System.objects.filter(id=sid)
                if system_obj:
                    system_obj = system_obj[0]
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 获得post数据
                name = request.POST.get('name')
                IMEI = request.POST.get('IMEI')
                if Device.objects.filter(system_id=sid, name=name):
                    return HttpResponse('444')
                else:
                    Device.objects.create(name=name, IMEI=IMEI, system=system_obj)
                    # 操作记录
                    Operation.objects.create(code=302, user=user_obj)
                return HttpResponse('666')
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def pushAdd(request, username, sid):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                # 系统对象
                system_obj = System.objects.filter(id=sid)
                if system_obj:
                    system_obj = system_obj[0]
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 获得post数据
                switch = request.POST.get('Switch')
                cycle = request.POST.get('Cycle')
                did = request.POST.get('did')
                device_obj = Device.objects.filter(id=did)
                if user_obj in system_obj.admin.all() or device_obj:
                    # 数据模板
                    type_name = eval(str(system_obj.type))
                    data_type = type_name.keys()
                    data = {}
                    for type in data_type:
                        if type == 'Switch':
                            data[type] = int(switch)
                        elif type == 'Cycle':
                            data[type] = cycle
                        else:
                            data[type] = 0

                    Data.objects.create(device=device_obj[0], model=1, data=str(data))
                    Operation.objects.create(code=305, user=user_obj)
                    return HttpResponse('666')
                else:
                    return HttpResponse('444')
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def pushAddAll(request, username, sid):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                # 系统对象
                system_obj = System.objects.filter(id=sid)
                if system_obj:
                    system_obj = system_obj[0]
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 获得post数据
                switch = request.POST.get('Switch')
                cycle = request.POST.get('Cycle')
                if user_obj in system_obj.admin.all():
                    # 数据模板
                    type_name = eval(str(system_obj.type))
                    data_type = type_name.keys()
                    data = {}
                    for type in data_type:
                        if type == 'Switch':
                            data[type] = int(switch)
                        elif type == 'Cycle':
                            data[type] = cycle
                        else:
                            data[type] = 0
                    for device_obj in system_obj.device.all():
                        Data.objects.create(device=device_obj, model=1, data=str(data))
                    Operation.objects.create(code=305, user=user_obj)
                    return HttpResponse('666')
                else:
                    return HttpResponse('444')
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def newDeviceMap(request, username, sid, did):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户

                # 拿到用户ORM对象
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 有无异常设备
                waring_system_list, waring_device_list = waringDevice(user_obj)
                user_name = user_obj.name
                # 系统对象
                system_obj = System.objects.filter(id=sid)
                if system_obj:
                    system_obj = system_obj[0]
                else:
                    return HttpResponse('error')

                # 设备对象
                device_obj = Device.objects.filter(id=did)
                if device_obj:
                    device_obj = device_obj[0]
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))

                # 判断是否有管理权限

                if device_obj.system == system_obj:
                    pass
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))

                if user_obj in device_obj.system.admin.all() and system_obj.platform == 'Detritus':

                    # 数据模板
                    type_name = eval(str(system_obj.type))
                    data_type = type_name.keys()

                    device_map = {}

                    # 地图数据
                    data = eval(str(device_obj.data.filter(model=0).all().last()))

                    if data:
                        pass
                    else:
                        return render(request, 'system/noDataDetail.html', locals())

                    new_map_data = {}

                    for key_data, value_data in data.items():
                        if key_data in data_type:
                            device_map[key_data] = value_data

                    new_map_data['data'] = device_map
                    new_map_data['name'] = device_obj.name

                    if device_obj.data.filter(waring=1, model=0):
                        waring_data = device_obj.data.filter(waring=1, model=0).last()
                        new_map_data['status'] = 'waring'
                    else:
                        new_map_data['status'] = 'running'

                    return HttpResponse(json.dumps(new_map_data))
                else:
                    return redirect('/admin/' + request.session.get('USERNAME'))
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
