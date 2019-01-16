from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
import hashlib


# Create your views here.

def admin(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USERNAME')
        domain_id = request.session.get('DOMAIN_ID')
        # 数据库交互
        # 未完成
        return render(request, 'admin.html', locals())
    else:
        return login(request)


def login(request):
    if request.method == "POST":
        domain = request.POST.get('domain')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 密码sha1加密
        password = hashlib.sha1(password.encode(encoding='utf8')).hexdigest()
        # 判断域
        user_domain_id = Domain.objects.filter(name=domain)
        if user_domain_id:
            domain_id = user_domain_id[0].id
            # 判断密码
            user_pwd = Users.objects.filter(username=username, domain_id=domain_id).values('password')
            if user_pwd:
                if user_pwd[0].password == password:
                    request.session['IS_LOGIN'] = True
                    request.session['USERNAME'] = username
                    request.session['DOMAIN_ID'] = domain_id
                    return HttpResponse('666')
                    # 登陆成功
                else:
                    return HttpResponse('555')
                    # 密码错误
            else:
                return HttpResponse('444')
                # 用户名错误
        else:
            return HttpResponse('333')
            # 域名错误

    if request.method == 'GET':
        login = '<ul class="login-ul"><li class="no-login-li" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">登陆</li><li class="no-login-li"><a target="_blank" href="/register" data-hmt-type="header_19" >注册</a></li></ul>'
        return render(request, 'index.html', locals())


def register(request):
    if request.method == "GET":
        pass
        return render(request, 'register.html', locals())
    if request.method == "POST":
        pass
        return render(request, 'register.html', locals())
