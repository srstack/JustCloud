import sys
import os
import random

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
    if waring in ['a', 'b', 'c']:
        return False
    else:
        return True


# jinger1
if waring():
    data = "{'Lon':'119.467','Lat':'32.1945','Switch':1,'Cycle':'6','Turn':0}"
    Data.objects.create(device_id=35, model=0, data=data)
else:
    data = "{'Lon':'119.467','Lat':'32.1945','Switch':1,'Cycle':'6','Turn':1}"
    Data.objects.create(device_id=35, model=0, data=data, waring=1)

# jinger3
if waring():
    data = "{'Lon':'119.460','Lat':'32.195','Switch':1,'Cycle':'6','Turn':0}"
    Data.objects.create(device_id=36, model=0, data=data)
else:
    data = "{'Lon':'119.460','Lat':'32.195','Switch':1,'Cycle':'6','Turn':0}"
    Data.objects.create(device_id=36, model=0, data=data, waring=1)

# jinger6
if waring():
    data = "{'Lon':'119.467','Lat':'32.196','Switch':1,'Cycle':'6','Turn':0}"
    Data.objects.create(device_id=8, model=0, data=data)
else:
    data = "{'Lon':'119.467','Lat':'32.196','Switch':1,'Cycle':'6','Turn':1}"
    Data.objects.create(device_id=8, model=0, data=data, waring=1)

# jinger7
if waring():
    data = "{'Lon':'119.465','Lat':'32.196','Switch':1,'Cycle':'6','Turn':0}"
    Data.objects.create(device_id=9, model=0, data=data)
else:
    data = "{'Lon':'119.465','Lat':'32.196','Switch':1,'Cycle':'6','Turn':0}"
    Data.objects.create(device_id=9, model=0, data=data, waring=1)

# detritus

if waring():
    data = "{'Lon':'119.4675','Lat':'32.1945','Switch':1,'Cycle':'6','Full':0}"
    Data.objects.create(device_id=12, model=0, data=data)
else:
    data = "{'Lon':'119.4675','Lat':'32.1945','Switch':1,'Cycle':'6','Full':1}"
    Data.objects.create(device_id=12, model=0, data=data, waring=1)

if waring():
    data = "{'Lon':'119.4655','Lat':'32.19605','Switch':1,'Cycle':'6','Full':0}"
    Data.objects.create(device_id=33, model=0, data=data)
else:
    data = "{'Lon':'119.4655','Lat':'32.19605','Switch':1,'Cycle':'6','Full':1}"
    Data.objects.create(device_id=33, model=0, data=data, waring=1)

if waring():
    data = "{'Lon':'119.4658','Lat':'32.1952','Switch':1,'Cycle':'6','Full':0}"
    Data.objects.create(device_id=14, model=0, data=data)
else:
    data = "{'Lon':'119.4658','Lat':'32.1952','Switch':1,'Cycle':'6','Full':1}"
    Data.objects.create(device_id=14, model=0, data=data, waring=1)
