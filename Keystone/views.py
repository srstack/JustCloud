from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
import hashlib


# Create your views here.
def home_no(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USERNAME')
        url = '/home/' + username
        return redirect(url)
    else:
        return render(request, 'waring_login.html')


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
            user_obj = Users.objects.filter(username=username)[0]
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            main_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '平台概况'
            # 用户设备数
            use_system = user_obj.system
            device_count = 0
            for i in use_system.all():
                device_count += Device.objects.filter(system=i).count()
            # 用户使用系统数
            system_count = user_obj.ownsystem.count()

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
            user_obj = Users.objects.filter(username=username)[0]
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            plat_admin_chose = 'active'
            # 确定menu选中
            device_admin = 'active'
            # 主体栏显示的部分
            exhibition_name = '设备管理'

            devices = []
            for system_obj in user_obj.system.all():
                for device_obj in system_obj.device.all():
                    devices.append(device_obj)

            return render(request, 'device.html', locals())
        else:
            return redirect('/admin/' + request.session.get('USERNAME') + '/device')
    else:
        return redirect('/')


def mainHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        # 浩民加油！！！
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户
            user_obj = Users.objects.filter(username=username)[0]
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
            user_obj = Users.objects.filter(username=username)[0]
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            user_center_chose = 'active'
            # 确定menu选中
            auth_home = 'active'
            # 主体栏显示的部分
            exhibition_name = '权限设置'

            system_list = System.objects.filter(admin=user_obj)
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
            user_obj = Users.objects.filter(username=username)[0]
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
                user_obj = Users.objects.filter(username=username)[0]
                domain = Domain.objects.filter(
                    id=request.session.get('DOMAIN_ID'))[0]
                if user_obj.rely:
                    return HttpResponse('222')
                else:
                    reg_domain = request.POST.get('domain')
                    reg_country = request.POST.get('country')
                    reg_province = request.POST.get('province')
                    reg_city = request.POST.get('city')
                    domain.name = reg_domain
                    domain.country = reg_country
                    domain.province = reg_province
                    domain.city = reg_city
                    domain.save()
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
                reg_username = request.POST.get('username')
                reg_name = request.POST.get('name')
                reg_pwd = request.POST.get('password')
                reg_tel = request.POST.get('tel')
                reg_email = request.POST.get('email')
                user_obj = Users.objects.filter(username=username)[0]
                domain = Domain.objects.filter(
                    id=request.session.get('DOMAIN_ID'))[0]
                username = Users.objects.filter(username=reg_username)
                if username:
                    # 用户存在
                    return HttpResponse('444')
                else:
                    username = Users.objects.filter(phone=reg_tel)
                    if username:
                        # 手机号存在
                        return HttpResponse('777')
                    else:
                        username = Users.objects.filter(email=reg_email)
                        if username:
                            # 邮箱存在
                            return HttpResponse('888')
                        else:
                            password = hashlib.sha1(
                                reg_pwd.encode(encoding='utf8')).hexdigest()
                            Users.objects.create(username=reg_username, password=password, name=reg_name,
                                                 domain=domain, rely=user_obj,
                                                 phone=reg_tel, email=reg_email)
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
                sub_obj = Users.objects.filter(
                    id=sub_id, rely=Users.objects.filter(username=username)[0])
                if sub_obj:
                    sub_obj.delete()
                    Operation.objects.create(
                        code=102, user=Users.objects.filter(username=username)[0])
                    return HttpResponse('666')
                else:
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
                sub_id = request.POST.get('uid')
                sys_id = request.POST.get('sid')
                sub_obj = Users.objects.filter(
                    id=sub_id, rely=Users.objects.filter(username=username)[0])
                if sub_obj:
                    sub_obj[0].system.remove(sys_id)
                    Operation.objects.create(code=205, user=Users.objects.filter(username=username)[0])
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
                sub_id = request.POST.get('sub_id')
                sys_id = request.POST.get('system_id')
                sys_obj = System.objects.filter(
                    id=sys_id, admin=Users.objects.filter(username=username)[0])
                if sys_obj:
                    if sys_obj[0].admin.filter(id=sub_id):
                        return HttpResponse('444')
                    else:
                        sys_obj[0].admin.add(sub_id)
                        Operation.objects.create(code=205, user=Users.objects.filter(username=username)[0])
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
                reg_name = request.POST.get('name')
                reg_phone = request.POST.get('phone')
                reg_email = request.POST.get('email')
                reg_age = request.POST.get('age')
                reg_sex = request.POST.get('sex')
                user_obj = Users.objects.filter(username=username)[0]

                if reg_name == user_obj.name:
                    if reg_email == user_obj.email:
                        if reg_phone == user_obj.phone:
                            user_obj.age = reg_age
                            user_obj.sex = reg_sex
                            user_obj.save()
                            Operation.objects.create(code=103, user=user_obj)
                            return HttpResponse('666')
                        else:
                            username = Users.objects.filter(phone=reg_phone)
                            if username:
                                # 手机号存在
                                return HttpResponse('777')
                            else:
                                user_obj.phone = reg_phone
                                user_obj.save()
                                Operation.objects.create(code=103, user=user_obj)
                                return HttpResponse('666')
                    else:
                        username = Users.objects.filter(email=reg_email)
                        if username:
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
                user_obj = Users.objects.filter(username=username)[0]
                old_pwd = request.POST.get('o_password')
                new_pwd = request.POST.get('password')
                if user_obj.password == hashlib.sha1(old_pwd.encode(encoding='utf8')).hexdigest():
                    user_obj.password = hashlib.sha1(new_pwd.encode(encoding='utf8')).hexdigest()
                    user_obj.save()
                    Operation.objects.create(code=103, user=user_obj)
                    del request.session['USERNAME']
                    del request.session['DOMAIN_ID']
                    request.session['IS_LOGIN'] = False
                    Login.objects.create(user=user_obj, operation='OUT', IP=request.META['REMOTE_ADDR'])
                    return HttpResponse('666')
                else:
                    return HttpResponse('777')
            else:
                return redirect('/home/' + request.session.get('USERNAME')+'/center')
        else:
            return redirect('/home/' + request.session.get('USERNAME')+'/center')
    else:
        return redirect('/')
