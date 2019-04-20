from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
import hashlib
import datetime
import random
from django.views.decorators.csrf import csrf_exempt
import json


# 生成设备注册码
def createCode():
    code = ''.join(random.sample(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'U', 'V', 'W', 'X',
         'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 15))
    return code


# 异常状态函数
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
def home_no(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USERNAME')
        url = '/home/' + username
        return redirect(url)
    else:
        return render(request, 'waring_login.html')


@csrf_exempt
def onenet(request):
    if request.method == 'GET':
        return HttpResponse(request.GET['msg'])

    else:
        msg = json.loads(request.body)['msg']
        imei = msg['imei']
        data = eval(msg['value'])
        print(msg, imei, data, data['Lat'])
        if Device.objects.filter(IMEI=imei):
            device_obj = Device.objects.filter(IMEI=imei)[0]
            if data['Full'] == 1:
                Data.objects.create(device=device_obj, model=0, data=msg['value'], waring=1)
                return HttpResponse("123")
            else:
                Data.objects.create(device=device_obj, model=0, data=msg['value'])
                return HttpResponse("123")
        else:
            return HttpResponse("123")


@csrf_exempt
def tlink(request):
    if request.method == 'POST':
        print(request.POST)


def admin_no(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USERNAME')
        url = '/admin/' + username
        return redirect(url)
    else:
        return render(request, 'waring_login.html')


def mainAdmin(request, username):
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
            exhibition_name = '平台概况'

            # 设备列表
            devices = []
            # 用户设备数
            for system_obj in user_obj.system.all():
                for device_obj in system_obj.device.all():
                    devices.append(device_obj)
            device_count = len(devices)

            # 系统列表
            system_list = System.objects.filter(admin=user_obj)
            # 系统个数
            system_count = system_list.count()
            # 今日时间
            now_date = str(datetime.datetime.now().date())
            # 今日推送数据列表
            today_push_data = []
            # 今日订阅数据列表
            today_pull_data = []
            for device_obj in devices:
                for data_obj in device_obj.data.all():
                    if str(data_obj.date).split()[0] == now_date:
                        if data_obj.model:
                            today_push_data.append(data_obj)
                        else:
                            today_pull_data.append(data_obj)

            # 今日推送数据数
            today_push_data_count = len(today_push_data)

            # 今日订阅消息数
            today_pull_data_count = len(today_pull_data)

            # 子系统饼状图
            system_type_dict = {'Jinger': 0, 'Detritus': 0, 'Lumiere': 0, 'Parquer': 0, 'Others': 0, }
            for system_obj in system_list:
                system_type_dict[str(system_obj.platform)] = system_type_dict[str(system_obj.platform)] + 1

            # 设备数柱状图
            device_count_dict = {'Jinger': 0, 'Detritus': 0, 'Lumiere': 0, 'Parquer': 0, 'Others': 0, }
            for system_obj in system_list:
                device_count_dict[str(system_obj.platform)] = device_count_dict[str(system_obj.platform)] + len(
                    system_obj.device.all())

            return render(request, 'admin.html', locals())
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def deviceAdmin(request, username):
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
            exhibition_name = '设备管理'

            # 系统列表
            system_list = System.objects.filter(admin=user_obj)
            # 管理设备列表
            devices = []
            for system_obj in user_obj.system.all():
                for device_obj in system_obj.device.all():
                    devices.append(device_obj)

            # 设备总数
            device_count = len(devices)

            # 今日时间
            now_date = str(datetime.datetime.now().date())

            # 活跃设备数
            device_active_count = 0
            for device_obj in devices:
                if device_obj.data.all():
                    if str(device_obj.data.last().date).split()[0] == now_date:
                        device_active_count = device_active_count + 1
            # 异常设备数
            device_waring_count = 0
            for device_obj in devices:
                if device_obj.data.filter(waring=1).all():
                    device_waring_count = device_waring_count + 1

            return render(request, 'deviceAdmin.html', locals())
        else:
            return redirect('/admin/' + request.session.get('USERNAME') + '/device')
    else:
        return redirect('/')


def deviceRemove(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                did = request.POST.get('did')

                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 设备对象
                device_obj = Device.objects.filter(id=did)[0]

                # 判断是否有管理权限(系统创建者和管理员)
                if (
                        device_obj.system.createuser == user_obj and user_obj in device_obj.system.admin.all()) or not user_obj.rely:
                    # 删除设备
                    device_obj.delete()
                    Operation.objects.create(
                        code=303,
                        user=user_obj)
                    return HttpResponse('666')
                else:
                    # 不属于user管理
                    return HttpResponse('555')
            else:
                return redirect('/admin/' + request.session.get('USERNAME') + '/device/')
        else:
            return redirect('/')
    else:
        return redirect('/')


def systemCreate(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 获得post数据
                name = request.POST.get('name')
                platform = request.POST.get('platform')
                type = request.POST.get('type')
                protocol = request.POST.get('protocol')
                code = createCode()
                # 判断模板
                if str(type).startswith('{\'Lon\':\'经度\',\'Lat\':\'纬度\',\'Switch\':\'设备状态\',\'Cycle\':\'订阅周期\','):
                    if System.objects.filter(domain_id=request.session.get('DOMAIN_ID'), name=name):
                        return HttpResponse('444')
                    else:
                        # 创建系统
                        System.objects.create(name=name, platform=platform, type=type, protocol=protocol,
                                              domain_id=request.session.get('DOMAIN_ID'), createuser=user_obj,
                                              devicecode=code)
                        # 增加管理权限
                        admin_user = user_obj
                        while True:
                            if admin_user.rely:
                                System.objects.filter(name=name, domain_id=request.session.get('DOMAIN_ID'))[
                                    0].admin.add(admin_user, admin_user.rely)
                                admin_user = admin_user.rely
                            else:
                                System.objects.filter(name=name, domain_id=request.session.get('DOMAIN_ID'))[
                                    0].admin.add(admin_user)
                                break
                        # 操作记录
                        Operation.objects.create(code=202, user=user_obj)
                    return HttpResponse('666')
                else:
                    return HttpResponse('222')
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def systemRemove(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                sid = request.POST.get('sid')
                # 用户对象
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 系统对象
                sys_obj = System.objects.filter(id=sid)[0]

                # 确定是否有权限删除系统（创建者或者管理员用户）
                if (sys_obj.createuser == user_obj and user_obj in sys_obj.admin.all()) or not user_obj.rely:
                    # 删除子用户
                    sys_obj.admin.clear()
                    sys_obj.delete()
                    Operation.objects.create(
                        code=203, user=user_obj)
                    return HttpResponse('666')
                else:
                    return HttpResponse('555')
            else:
                return redirect('/admin/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def deviceAdd(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 获得post数据
                name = request.POST.get('name')
                sid = request.POST.get('sid')
                IMEI = request.POST.get('IMEI')
                if Device.objects.filter(system_id=sid, name=name):
                    return HttpResponse('444')
                else:
                    Device.objects.create(name=name, IMEI=IMEI, system_id=sid)
                    # 操作记录
                    Operation.objects.create(code=302, user=user_obj)
                return HttpResponse('666')
            else:
                return redirect('/admin/' + request.session.get('USERNAME') + '/device/')
        else:
            return redirect('/')
    else:
        return redirect('/')


def mainHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        # 浩民加油！！！
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            domain = Domain.objects.filter(
                id=request.session.get('DOMAIN_ID'))[0]
            domain_name = domain.name
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            user_center_chose = 'active'
            # 确定menu选中
            main_home = 'active'
            # 主体栏显示的部分
            exhibition_name = '用户管理'
            user_leve = 1
            dic_user = {
                1: '管理员用户',
                2: '二级用户',
                3: '三级用户',
                4: '四级用户',
                5: '五级用户',
                6: '六级用户',
            }
            sub_user = user_obj
            while True:
                if sub_user.rely_id:
                    sub_user = sub_user.rely
                    user_leve = user_leve + 1
                else:
                    user_class = dic_user.get(user_leve)
                    break

            # 下级用户
            sub_user = Users.objects.filter(rely_id=user_obj.id)
            sub_user_count = sub_user.count()
            system_count = user_obj.system.count()
            return render(request, 'home.html', locals())
        else:
            return redirect('/home/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def authHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            user_center_chose = 'active'
            # 确定menu选中
            auth_home = 'active'
            # 主体栏显示的部分
            exhibition_name = '权限设置'

            # 系统列表
            system_list = System.objects.filter(admin=user_obj)
            # 系统个数
            system_count = system_list.count()

            sub_user = Users.objects.filter(rely=user_obj)
            return render(request, 'authHome.html', locals())
        else:
            return redirect('/home/' + request.session.get('USERNAME') + '/auth')
    else:
        return redirect('/')


def centerHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户
            user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
            # 有无异常设备
            waring_system_list, waring_device_list = waringDevice(user_obj)
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            user_center_chose = 'active'
            # 确定menu选中
            center_home = 'active'
            # 主体栏显示的部分
            exhibition_name = '个人中心'
            return render(request, 'centerHome.html', locals())
        else:
            return redirect('/home/' + request.session.get('USERNAME') + '/center')
    else:
        return redirect('/')


def domainChange(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                domain = Domain.objects.filter(
                    id=request.session.get('DOMAIN_ID'))[0]
                # 判断是否为管理员用户
                if user_obj.rely:
                    return HttpResponse('222')
                else:
                    # 修改域
                    reg_domain = request.POST.get('domain')
                    reg_country = request.POST.get('country')
                    reg_province = request.POST.get('province')
                    reg_city = request.POST.get('city')
                    domain.name = reg_domain
                    domain.country = reg_country
                    domain.province = reg_province
                    domain.city = reg_city
                    domain.save()
                    # 操作记录
                    Operation.objects.create(code=100, user=user_obj)
                    return HttpResponse('666')
            else:
                return redirect('/home/' + request.session.get('USERNAME') + '/center')
        else:
            return redirect('/')
    else:
        return redirect('/home')


def userAdd(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户

                # 获取post数据
                reg_username = request.POST.get('username')
                reg_name = request.POST.get('name')
                reg_pwd = request.POST.get('password')
                reg_tel = request.POST.get('tel')
                reg_email = request.POST.get('email')
                # 用户对象
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 所属域对象
                domain = Domain.objects.filter(
                    id=request.session.get('DOMAIN_ID'))[0]
                new_user = Users.objects.filter(username=reg_username, domain_id=request.session.get('DOMAIN_ID'))
                if new_user:
                    # 用户存在
                    return HttpResponse('444')
                else:
                    new_user = Users.objects.filter(phone=reg_tel)
                    if new_user:
                        # 手机号存在
                        return HttpResponse('777')
                    else:
                        new_user = Users.objects.filter(email=reg_email)
                        if new_user:
                            # 邮箱存在
                            return HttpResponse('888')
                        else:
                            # hash 密码
                            password = hashlib.sha1(
                                reg_pwd.encode(encoding='utf8')).hexdigest()
                            # 创建子用户
                            Users.objects.create(username=reg_username, password=password, name=reg_name,
                                                 domain=domain, rely=user_obj,
                                                 phone=reg_tel, email=reg_email)
                            # 操作记录
                            Operation.objects.create(code=101, user=user_obj)
                            return HttpResponse('666')
            else:
                return redirect('/home/' + request.session.get('USERNAME') + '/center')
        else:
            return redirect('/')
    else:
        return redirect('/')


def userRemove(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                sub_id = request.POST.get('id')
                # 子用户对象
                sub_obj = Users.objects.filter(
                    id=sub_id,
                    rely=Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0])
                if sub_obj:
                    # 删除子用户
                    sub_obj.delete()
                    Operation.objects.create(
                        code=102,
                        user=Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0])
                    return HttpResponse('666')
                else:
                    # 不属于user管理
                    return HttpResponse('555')
            else:
                return redirect('/home/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def adminRemove(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户

                # 获得post数据
                sub_id = request.POST.get('uid')
                sys_id = request.POST.get('sid')
                # 下级用户对象
                sub_obj = Users.objects.filter(
                    id=sub_id,
                    rely=Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0])
                if sub_obj:
                    # 删除管理权限
                    sub_obj[0].system.remove(sys_id)
                    Operation.objects.create(code=205, user=
                    Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0])
                    return HttpResponse('666')
                else:
                    return HttpResponse('555')
            else:
                return redirect('/home/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def adminAdd(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户

                # 获得post数据
                sub_id = request.POST.get('sub_id')
                sys_id = request.POST.get('system_id')
                # 系统对象
                sys_obj = System.objects.filter(
                    id=sys_id,
                    admin=Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0])
                if sys_obj:
                    # 存在管理权限
                    if sys_obj[0].admin.filter(id=sub_id):
                        return HttpResponse('444')
                    else:
                        # 添加管理权限
                        sys_obj[0].admin.add(sub_id)
                        # 操作记录
                        Operation.objects.create(code=205, user=
                        Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0])
                        return HttpResponse('666')
                else:
                    return HttpResponse('555')
            else:
                return redirect('/home/' + request.session.get('USERNAME'))
        else:
            return redirect('/')
    else:
        return redirect('/')


def userChange(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户

                # 获得post数据
                reg_name = request.POST.get('name')
                reg_phone = request.POST.get('phone')
                reg_email = request.POST.get('email')
                reg_age = request.POST.get('age')
                reg_sex = request.POST.get('sex')
                # 获得用户对象
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                # 判断用户名
                if reg_name == user_obj.name:
                    # 判断邮箱
                    if reg_email == user_obj.email:
                        # 判断手机
                        if reg_phone == user_obj.phone:
                            if not reg_age:
                                reg_age = 0
                            # 修改
                            Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID')).update(
                                sex=reg_sex, age=reg_age)
                            # 操作记录
                            Operation.objects.create(code=103, user=user_obj)
                            return HttpResponse('666')
                        else:
                            user_exist = Users.objects.filter(phone=reg_phone)
                            if user_exist:
                                # 手机号存在
                                return HttpResponse('777')
                            else:
                                user_obj.phone = reg_phone
                                user_obj.save()
                                Operation.objects.create(code=103, user=user_obj)
                                return HttpResponse('666')
                    else:
                        user_exist = Users.objects.filter(email=reg_email)
                        if user_exist:
                            # 邮箱存在
                            return HttpResponse('888')
                        else:
                            user_obj.email = reg_email
                            user_obj.save()
                            Operation.objects.create(code=103, user=user_obj)
                            return HttpResponse('666')
                else:
                    user_obj.name = reg_name
                    user_obj.save()
                    Operation.objects.create(code=103, user=user_obj)
                    return HttpResponse('666')
            else:
                return redirect('/home/' + request.session.get('USERNAME') + '/center')
        else:
            return redirect('/home/' + request.session.get('USERNAME') + '/center')
    else:
        return redirect('/')


def passwordChange(request, username):
    if request.method == 'POST':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            if request.session.get('USERNAME') == username:
                # 判断是否为此用户
                user_obj = Users.objects.filter(username=username, domain_id=request.session.get('DOMAIN_ID'))[0]
                old_pwd = request.POST.get('o_password')
                new_pwd = request.POST.get('password')
                # 判断旧密码是否正确
                if user_obj.password == hashlib.sha1(old_pwd.encode(encoding='utf8')).hexdigest():
                    # 修改密码
                    user_obj.password = hashlib.sha1(new_pwd.encode(encoding='utf8')).hexdigest()
                    user_obj.save()
                    Operation.objects.create(code=103, user=user_obj)
                    # 消除session登陆
                    del request.session['USERNAME']
                    del request.session['DOMAIN_ID']
                    request.session['IS_LOGIN'] = False
                    # 记录操作
                    Operation.objects.create(code=103, user=user_obj)
                    Login.objects.create(user=user_obj, operation='OUT', IP=request.META['REMOTE_ADDR'])
                    return HttpResponse('666')
                else:
                    return HttpResponse('777')
            else:
                return redirect('/home/' + request.session.get('USERNAME') + '/center')
        else:
            return redirect('/home/' + request.session.get('USERNAME') + '/center')
    else:
        return redirect('/')


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


def getwaring(request):
    if request.method == 'GET':
        is_login = request.session.get('IS_LOGIN', False)
        if is_login:
            # 获取系统对象
            user_obj = \
            Users.objects.filter(username=request.session.get('USERNAME'), domain_id=request.session.get('DOMAIN_ID'))[
                0]
            waring_system_list, waring_device_list = waringDevice(user_obj)
            if waring_device_list or waring_device_list:
                return HttpResponse('yes')
            else:
                return HttpResponse('no')
        else:
            return redirect('/')
    else:
        return redirect('/')
