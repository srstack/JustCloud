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
            domain = Domain.objects.filter(id=request.session.get('DOMAIN_ID'))[0]
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
                1:'管理员用户',
                2:'二级用户',
                3:'三级用户',
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

            sub_user_count = user_obj.sub_user.count()
            system_count = user_obj.system.count()
            return render(request, 'home.html', locals())
        else:
            return redirect('/home/' + request.session.get('USERNAME'))
    else:
        return redirect('/')


def authHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        # 浩民加油！！！
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
            return render(request, 'authHome.html', locals())
        else:
            return redirect('/home/' + request.session.get('USERNAME') + '/auth')
    else:
        return redirect('/')


def centerHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        # 浩民加油！！！
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
