from django.shortcuts import render, HttpResponse, redirectfrom SqlMaster.models import *import hashlib# Create your views here.def admin(request):    is_login = request.session.get('IS_LOGIN', False)    if is_login:        username = request.session.get('USERNAME')        url = '/admin/'+username        return redirect(url)    else:        return render(request, 'waring_login.html')def home(request):    is_login = request.session.get('IS_LOGIN', False)    if is_login:        username = request.session.get('USERNAME')        url = '/home/' + username        return redirect(url)    else:        return render(request, 'waring_login.html')