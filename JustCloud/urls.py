"""JustCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Dashboard import views as dashboard
from Detritus import views as detritus
from Keystone import views as keystone
from Lumiere import views as lumiere
from Parquer import views as parquer
from Jinger import views as jinger

urlpatterns = [
    path('databaseadmin/', admin.site.urls),
    path('dome/', dashboard.dome),  # 测试效果页面....
    path('', dashboard.index, name='index'),
    path('register/', dashboard.register, name="register"),
    path('admin/', keystone.admin_no, name='admin_on'),
    path('login/', dashboard.login, name='login'),
    path('logout/', dashboard.logout, name='logout'),
    path('home/', keystone.home_no, name='home_no'),
    path('admin/<username>/', keystone.mainAdmin, name='mainAdmin'),
    path('admin/<username>/systemcreate/', keystone.systemCreate, name='systemCreate'),
    path('admin/<username>/systemremove/', keystone.systemRemove, name='systemRemove'),
    path('admin/<username>/device/', keystone.deviceAdmin, name='deviceAdmin'),
    path('admin/<username>/device/deviceremove/', keystone.deviceRemove, name='deviceRemove'),
    path('admin/<username>/device/deviceadd/', keystone.deviceAdd, name='deviceAdd'),
    path('home/<username>/', keystone.mainHome, name='mainHome'),
    path('home/<username>/auth/', keystone.authHome, name='authHome'),
    path('home/<username>/center/', keystone.centerHome, name='centerHome'),
    path('home/<username>/domainchange/', keystone.domainChange, name='domainChange'),
    path('home/<username>/useradd/', keystone.userAdd, name='userAdd'),
    path('home/<username>/center/userchange/', keystone.userChange, name='userChange'),
    path('home/<username>/userremove/', keystone.userRemove, name='userRemove'),
    path('home/<username>/auth/adminremove/', keystone.adminRemove, name='adminRemove'),
    path('home/<username>/auth/adminadd/', keystone.adminAdd, name='adminAdd'),
    path('home/<username>/center/passwordchange/', keystone.passwordChange, name='passwordChange'),
    path('system/<username>/Jinger/<int:sid>/', jinger.systemMain, name='JingerMain'),
]
