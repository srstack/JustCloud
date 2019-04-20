import sys
import os
import random
import time

# 导入系统变量和环境变量
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JustCloud.settings")

# 导入django模块
import django

django.setup()

# 引入Model

from SqlMaster.models import *


# 是否异常函数

def waring():
    waring = ''.join(random.sample(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'U', 'V', 'W',
         'X',
         'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 1))
    if waring in ['a']:
        return False
    else:
        return True


# 睡眠函数
def sleep():
    time.sleep(random.randint(10, 3600))


sleep()
if waring():
    data1 = "{'Lon':'119.4621','Lat':'32.20029','Switch':1,'Cycle':'5','Switch-Light':0,'Top-Light':1,'Bottom-Light':0}"
    Data.objects.create(device_id=22, model=0, data=data1)
    data2 = "{'Lon':'119.4621','Lat':'32.20000','Switch':1,'Cycle':'5','Switch-Light':0,'Top-Light':1,'Bottom-Light':0}"
    Data.objects.create(device_id=23, model=0, data=data2)
else:
    data1 = "{'Lon':'119.4621','Lat':'32.20029','Switch':1,'Cycle':'5','Switch-Light':0,'Top-Light':1,'Bottom-Light':1}"
    Data.objects.create(device_id=22, model=0, data=data1, waring=1)
    data2 = "{'Lon':'119.4621','Lat':'32.20000','Switch':1,'Cycle':'5','Switch-Light':0,'Top-Light':1,'Bottom-Light':1}"
    Data.objects.create(device_id=23, model=0, data=data2)
