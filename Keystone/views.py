from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *
import  hashlib
# Create your views here.
# pwd = Users.objects.filter(username=15002837903).values("password")[0]
# hashlib.sha1(pwd[0].encode(encoding='utf8')).hexdigest()== pwd[0]

def admin(request):
    return HttpResponse("敬请期待")

def login(request):
    if request.method == "POST":
        print(request.POST['domain'])
        return HttpResponse('success')
    if request.method == 'GET':
        login = '<ul class="login-ul"><li class="no-login-li" data-toggle="modal" data-target="#exampleModal" data-whatever="@mdo">登陆</li><li class="no-login-li"><a target="_blank" href="/register" data-hmt-type="header_19" >注册</a></li></ul>'
        return render(request, 'index.html', locals())

def register(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass
    return redirect()