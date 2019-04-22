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
from Others import views as other

urlpatterns = [
    path('databaseadmin/', admin.site.urls),
    path('dome/', dashboard.dome),  # 测试效果页面....
    path('', dashboard.index, name='index'),
    path('register/', dashboard.register, name="register"),
    path('admin/', keystone.admin_no, name='admin_on'),
    path('login/', dashboard.login, name='login'),
    path('logout/', dashboard.logout, name='logout'),
    path('home/', keystone.home_no, name='home_no'),
    path('onenet/', keystone.onenet, name="onenet"),
    path('getwaring/', keystone.getwaring, name="getwaring"),
    path('api/onenet/', keystone.onenetDataIn, name="oneNETDataIn"),
    path('api/test/', keystone.onenetDataTest, name="apiTest"),
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
    path('system/<username>/Jinger/<int:sid>/analy/', jinger.systemAnaly, name='JingerAnaly'),
    path('system/<username>/Jinger/<int:sid>/analy/waringremove/', jinger.waringRemove, name='waringRemove'),
    path('system/<username>/Jinger/<int:sid>/device/', jinger.systemDevice, name='systemDevice'),
    path('system/<username>/Jinger/<int:sid>/device/deviceremove/', jinger.deviceRemove, name='deviceRemove'),
    path('system/<username>/Jinger/<int:sid>/device/deviceadd/', jinger.deviceAdd, name='deviceAdd'),
    path('system/<username>/Jinger/<int:sid>/device/<int:did>/', jinger.deviceDetail, name='deviceDetail'),
    path('system/<username>/Jinger/<int:sid>/device/<int:did>/getnewdevicemap/', jinger.newDeviceMap,
         name='newDeviceMap'),
    path('system/<username>/Jinger/<int:sid>/device/<int:did>/waringremove/', jinger.waringRemove, name='waringRemove'),
    path('system/<username>/Jinger/<int:sid>/type/', jinger.dataType, name='dataType'),
    path('system/<username>/Jinger/<int:sid>/push/', jinger.systemPush, name='systemPush'),
    path('system/<username>/Jinger/<int:sid>/push/pushadd/', jinger.pushAdd, name='pushAdd'),
    path('system/<username>/Jinger/<int:sid>/push/pushaddall/', jinger.pushAddAll, name='pushAddAll'),
    path('system/<username>/Jinger/<int:sid>/pull/', jinger.systemPull, name='systemPull'),
    path('system/<username>/Detritus/<int:sid>/', detritus.systemMain, name='DetritusMain'),
    path('system/<username>/Detritus/<int:sid>/analy/', detritus.systemAnaly, name='DetritusAnaly'),
    path('system/<username>/Detritus/<int:sid>/analy/waringremove/', detritus.waringRemove, name='waringRemove'),
    path('system/<username>/Detritus/<int:sid>/device/', detritus.systemDevice, name='systemDevice'),
    path('system/<username>/Detritus/<int:sid>/device/deviceremove/', detritus.deviceRemove, name='deviceRemove'),
    path('system/<username>/Detritus/<int:sid>/device/deviceadd/', detritus.deviceAdd, name='deviceAdd'),
    path('system/<username>/Detritus/<int:sid>/device/<int:did>/', detritus.deviceDetail, name='deviceDetail'),
    path('system/<username>/Detritus/<int:sid>/device/<int:did>/getnewdevicemap/', detritus.newDeviceMap,
         name='newDeviceMap'),
    path('system/<username>/Detritus/<int:sid>/device/<int:did>/waringremove/', detritus.waringRemove,
         name='waringRemove'),
    path('system/<username>/Detritus/<int:sid>/type/', detritus.dataType, name='dataType'),
    path('system/<username>/Detritus/<int:sid>/push/', detritus.systemPush, name='systemPush'),
    path('system/<username>/Detritus/<int:sid>/push/pushadd/', detritus.pushAdd, name='pushAdd'),
    path('system/<username>/Detritus/<int:sid>/push/pushaddall/', detritus.pushAddAll, name='pushAddAll'),
    path('system/<username>/Detritus/<int:sid>/pull/', detritus.systemPull, name='systemPull'),
    path('system/<username>/Lumiere/<int:sid>/', lumiere.systemMain, name='LumiereMain'),
    path('system/<username>/Lumiere/<int:sid>/analy/', lumiere.systemAnaly, name='LumiereAnaly'),
    path('system/<username>/Lumiere/<int:sid>/analy/waringremove/', lumiere.waringRemove, name='waringRemove'),
    path('system/<username>/Lumiere/<int:sid>/device/', lumiere.systemDevice, name='systemDevice'),
    path('system/<username>/Lumiere/<int:sid>/device/deviceremove/', lumiere.deviceRemove, name='deviceRemove'),
    path('system/<username>/Lumiere/<int:sid>/device/deviceadd/', lumiere.deviceAdd, name='deviceAdd'),
    path('system/<username>/Lumiere/<int:sid>/device/<int:did>/', lumiere.deviceDetail, name='deviceDetail'),
    path('system/<username>/Lumiere/<int:sid>/device/<int:did>/getnewdevicemap/', lumiere.newDeviceMap,
         name='newDeviceMap'),
    path('system/<username>/Lumiere/<int:sid>/device/<int:did>/waringremove/', lumiere.waringRemove,
         name='waringRemove'),
    path('system/<username>/Lumiere/<int:sid>/type/', lumiere.dataType, name='dataType'),
    path('system/<username>/Lumiere/<int:sid>/push/', lumiere.systemPush, name='systemPush'),
    path('system/<username>/Lumiere/<int:sid>/push/pushadd/', lumiere.pushAdd, name='pushAdd'),
    path('system/<username>/Lumiere/<int:sid>/push/pushaddall/', lumiere.pushAddAll, name='pushAddAll'),
    path('system/<username>/Lumiere/<int:sid>/pull/', lumiere.systemPull, name='systemPull'),
    path('system/<username>/Parquer/<int:sid>/', parquer.systemMain, name='ParquerMain'),
    path('system/<username>/Parquer/<int:sid>/analy/', parquer.systemAnaly, name='ParquerAnaly'),
    path('system/<username>/Parquer/<int:sid>/analy/waringremove/', parquer.waringRemove, name='waringRemove'),
    path('system/<username>/Parquer/<int:sid>/analy/getfreecount/', parquer.freeCount, name='freeCount'),
    path('system/<username>/Parquer/<int:sid>/device/', parquer.systemDevice, name='systemDevice'),
    path('system/<username>/Parquer/<int:sid>/device/deviceremove/', parquer.deviceRemove, name='deviceRemove'),
    path('system/<username>/Parquer/<int:sid>/device/deviceadd/', parquer.deviceAdd, name='deviceAdd'),
    path('system/<username>/Parquer/<int:sid>/device/<int:did>/', parquer.deviceDetail, name='deviceDetail'),
    path('system/<username>/Parquer/<int:sid>/device/<int:did>/getnewdevicemap/', parquer.newDeviceMap,
         name='newDeviceMap'),
    path('system/<username>/Parquer/<int:sid>/device/<int:did>/waringremove/', parquer.waringRemove,
         name='waringRemove'),
    path('system/<username>/Parquer/<int:sid>/type/', parquer.dataType, name='dataType'),
    path('system/<username>/Parquer/<int:sid>/push/', parquer.systemPush, name='systemPush'),
    path('system/<username>/Parquer/<int:sid>/push/pushadd/', parquer.pushAdd, name='pushAdd'),
    path('system/<username>/Parquer/<int:sid>/push/pushaddall/', parquer.pushAddAll, name='pushAddAll'),
    path('system/<username>/Parquer/<int:sid>/pull/', parquer.systemPull, name='systemPull'),
    path('system/<username>/Others/<int:sid>/', other.systemMain, name='JingerMain'),
    path('system/<username>/Others/<int:sid>/analy/', other.systemAnaly, name='JingerAnaly'),
    path('system/<username>/Others/<int:sid>/analy/waringremove/', other.waringRemove, name='waringRemove'),
    path('system/<username>/Others/<int:sid>/device/', other.systemDevice, name='systemDevice'),
    path('system/<username>/Others/<int:sid>/device/deviceremove/', other.deviceRemove, name='deviceRemove'),
    path('system/<username>/Others/<int:sid>/device/deviceadd/', other.deviceAdd, name='deviceAdd'),
    path('system/<username>/Others/<int:sid>/device/<int:did>/', other.deviceDetail, name='deviceDetail'),
    path('system/<username>/Others/<int:sid>/device/<int:did>/getnewdevicemap/', other.newDeviceMap,
         name='newDeviceMap'),
    path('system/<username>/Others/<int:sid>/device/<int:did>/waringremove/', other.waringRemove, name='waringRemove'),
    path('system/<username>/Others/<int:sid>/type/', other.dataType, name='dataType'),
    path('system/<username>/Others/<int:sid>/push/', other.systemPush, name='systemPush'),
    path('system/<username>/Others/<int:sid>/push/pushadd/', other.pushAdd, name='pushAdd'),
    path('system/<username>/Others/<int:sid>/push/pushaddall/', other.pushAddAll, name='pushAddAll'),
    path('system/<username>/Others/<int:sid>/pull/', other.systemPull, name='systemPull'),

]
