from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
import datetime


def waringDevice(user_obj):
    devices = []
    system = []
    waring_devices = []
    for system_obj in user_obj.system.all():
        for device_obj in system_obj.device.all():
            devices.append(device_obj)
    for device_obj in devices:
        if device_obj.data.filter(waring=1).all():
            system.append(device_obj.system)
            waring_devices.append(device_obj)
    return system, waring_devices


# Create your views here.

# 模板函数
def systemType(request, username, sid):
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
            system_obj = System.objects.filter(id=sid)[0]
            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Jinger':
                # 设备queryset
                devices = system_obj.device.all()
                device_count = len(devices)
                return render(request, 'Jinger/jingerAnaly.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


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
            system_obj = System.objects.filter(id=sid)[0]

            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Jinger':

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
                now_time = datetime.datetime.now().date()
                now_date = str(now_time)

                # 最近五天
                time_list = [now_date, ]
                tmp_time = now_time
                yes_time = datetime.timedelta(days=-1)
                for i in range(0, 4):
                    time_list.append(str(tmp_time + yes_time))
                    tmp_time = tmp_time + yes_time
                time_list.reverse()

                data_push_list = [0, 0, 0, 0, 0]
                data_pull_list = [0, 0, 0, 0, 0]

                new_devices = []
                for device in devices:
                    if device.data.all():
                        device_active_list.append(device)
                    else:
                        device_inactive_list.append(device)
                    if str(device.date).split()[0] == now_date:
                        new_devices.append(device)
                    data_count = data_count + len(device.data.all())
                    for data in device.data.all():
                        if data.model:
                            push_count = push_count + 1
                        else:
                            pull_count = pull_count + 1
                        if str(data.date).split()[0] == now_date:
                            new_data_count = new_data_count + 1
                        for i in range(0, 5):
                            if str(data.date).split()[0] == time_list[i]:
                                if data.model:
                                    data_push_list[i] = data_push_list[i] + 1
                                else:
                                    data_pull_list[i] = data_pull_list[i] + 1
                device_active_count = len(device_active_list)
                device_inactive_count = len(device_inactive_list)
                new_devices_count = len(new_devices)
                new_device_active = 0
                new_device_inactive = 0
                for device in new_devices:
                    if device in device_active_list:
                        new_device_active = new_device_active + 1
                    else:
                        new_device_inactive = new_device_inactive + 1

                return render(request, 'Jinger/jingerMain.html', locals())
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
            system_obj = System.objects.filter(id=sid)[0]
            # 判断是否有管理权限
            if user_obj in system_obj.admin.all() and system_obj.platform == 'Jinger':
                # 设备queryset
                devices = system_obj.device.all()
                device_count = len(devices)
                return render(request, 'Jinger/jingerAnaly.html', locals())
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')
