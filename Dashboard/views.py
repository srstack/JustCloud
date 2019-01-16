from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *


# Create your views here.

def index(request):
    user = request.META["OS"]
    print(request.META["OS"])
    login = '<ul class="login-ul"><li class="no-login-li" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">登陆</li><li class="no-login-li"><a target="_blank" href="/register" data-hmt-type="header_19" >注册</a></li></ul>'
    if str(user).startswith("Windows_NT"):
        return render(request, 'index.html', locals())
    else:
        return HttpResponse("尽情期待")


def dome(request):
    return render(request, 'dome.html')
