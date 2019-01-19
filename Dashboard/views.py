from django.shortcuts import render, HttpResponse, redirect
from SqlMaster.models import *


# Create your views here.

def index(request):
    user = request.META["OS"]
    print(request.META["OS"])
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USERNAME')
        print(username)
        user_name = Users.objects.filter(username=username).values('name')[0].get('name')
        first_name = user_name[0]
        return render(request, 'index_login.html', locals())
    else:
        if str(user).startswith("Windows_NT"):
            return render(request, 'index.html')
        else:
            return HttpResponse("尽情期待")


def dome(request):
    return render(request, 'dome.html')
