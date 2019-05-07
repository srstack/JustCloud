from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
import hashlib


# Create your views here.

def index(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USERNAME')
        user_name = Users.objects.filter(username=username).values('name')[0].get('name')
        first_name = user_name[0]
        return render(request, 'index_login.html', locals())
    else:
        return render(request, 'index.html')


def login(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        return redirect('/')
    else:
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
                user_obj = Users.objects.filter(username=username, domain_id=domain_id).values('password', 'id')
                if user_obj:
                    if user_obj[0].get('password') == password:
                        request.session['IS_LOGIN'] = True
                        request.session['USERNAME'] = username
                        request.session['DOMAIN_ID'] = domain_id
                        Login.objects.create(user_id=user_obj[0].get('id'), operation='IN',
                                             IP=request.META['REMOTE_ADDR'])
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
            return redirect('/')


def register(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        return redirect('/')
    else:
        if request.method == "GET":
            return render(request, 'register.html', locals())
        if request.method == "POST":
            reg_code = request.POST.get('code')
            reg_domain = request.POST.get('domain')
            reg_country = request.POST.get('country')
            reg_province = request.POST.get('province')
            reg_city = request.POST.get('city')
            reg_username = request.POST.get('username')
            reg_name = request.POST.get('name')
            reg_pwd = request.POST.get('password')
            reg_tel = request.POST.get('tel')
            reg_email = request.POST.get('email')
            domain = Domain.objects.filter(name=reg_domain)
            if reg_code in ['qsrnbqsrnb', 'chmnbchmnb']:
                if domain:
                    # 域存在
                    return HttpResponse('333')
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
                            password = hashlib.sha1(reg_pwd.encode(encoding='utf8')).hexdigest()
                            Domain.objects.create(name=reg_domain, city=reg_city, province=reg_province,
                                                  country=reg_country)
                            domain_obj = Domain.objects.get(name=reg_domain)
                            Users.objects.create(username=reg_username, password=password, name=reg_name,
                                                 domain=domain_obj,
                                                 phone=reg_tel, email=reg_email)
                            user_obj = Users.objects.get(username=reg_username, domain=domain_obj)
                            request.session['IS_LOGIN'] = True
                            request.session['USERNAME'] = reg_username
                            request.session['DOMAIN_ID'] = domain_obj.id
                            Operation.objects.create(code=101, user=user_obj)
                            Operation.objects.create(code=900, user=user_obj)
                            Login.objects.create(user=user_obj, operation='IN', IP=request.META['REMOTE_ADDR'])
                            return HttpResponse('666')
            else:
                # 激活码错误
                return HttpResponse('555')


def logout(request):
    request.session['IS_LOGIN'] = False
    user_obj = Users.objects.get(username=request.session.get('USERNAME'), domain_id=request.session.get('DOMAIN_ID'))
    del request.session['USERNAME']
    del request.session['DOMAIN_ID']
    Login.objects.create(user=user_obj, operation='OUT', IP=request.META['REMOTE_ADDR'])
    return redirect('/')


def dome(request):
    return render(request, 'dome.html')
