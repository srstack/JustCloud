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

            user_name=username
            first_name=user_name[0]
            return render(request,'admin.html',locals())
        else:
            return redirect('/admin/' + request.session.get('USERNAME'))
    else:
        return redirect('/register')


def mainHome(request, username):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        # 浩民加油！！！
        if request.session.get('USERNAME') == username:
            # 判断是否为此用户

            # 浩民加油
            return HttpResponse(username+'的家')
        else:
            return redirect('/home/' + request.session.get('USERNAME'))
    else:
        return redirect('/')
