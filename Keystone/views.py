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

            # 左侧列表显示栏——名称：{awesome图标类：跳转URL}
            menu_list = {
                '平台概况': {'fa-linode': '/admin'},
                '设备管理': {'fa-cubes': '/admin/' + username + '/device'},
            }

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

            # 左侧列表显示栏——名称：{awesome图标类：跳转URL}
            menu_list = {
                '平台概况': {'fa-linode': '/admin'},
                '设备管理': {'fa-cubes': '/admin/' + username + '/device'},
            }

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
            user_name = user_obj.name
            first_name = user_name[0]
            # 确定header选中
            user_center_chose = 'active'

            menu_list = {
                '用户管理': {'fa-eercast': '/home'},
                '权限设置': {'fa-bullseye': '/home/' + username + '/auth'},
                '个人中心': {'fa-cogs': '/home/' + username + '/center'},
            }

            # 主体栏显示的部分
            exhibition_name = '用户管理'

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

            menu_list = {
                '用户管理': {'fa-eercast': '/home'},
                '权限设置': {'fa-bullseye': '/home/' + username + '/auth'},
                '个人中心': {'fa-cogs': '/home/' + username + '/center'},
            }

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

            menu_list = {
                '用户管理': {'fa-eercast': '/home'},
                '权限设置': {'fa-bullseye': '/home/' + username + '/auth'},
                '个人中心': {'fa-cogs': '/home/' + username + '/center'},
            }

            # 主体栏显示的部分
            exhibition_name = '个人中心'

            return render(request, 'centerHome.html', locals())
        else:
            return redirect('/home/' + request.session.get('USERNAME') + '/center')
    else:
        return redirect('/')
