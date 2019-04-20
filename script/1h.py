import sys
import os
import random
import time

# 多线程保证子任务同时执行
from threading import Thread

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
    if waring in ['a', '5', '6', '7', 'B', 'C','i', 'j', 'k', 'm']:
        return True
    else:
        return False


def jwaring():
    waring = ''.join(random.sample(
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'U', 'V', 'W',
         'X',
         'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 1))
    if waring in ['a', '5']:
        return True
    else:
        return False


# 睡眠函数
def sleep():
    time.sleep(random.randint(10, 6400))


# jinger
def jin1():
    sleep()
    if jwaring():
        data = "{'Lon':'119.467','Lat':'32.1945','Switch':1,'Cycle':'6','Turn':1}"
        Data.objects.create(device_id=2, model=0, data=data, waring=1)


# jinger3
def jin3():
    sleep()
    if jwaring():
        data = "{'Lon':'119.460','Lat':'32.195','Switch':1,'Cycle':'6','Turn':0}"
        Data.objects.create(device_id=4, model=0, data=data, waring=1)


# jinger6
def jin6():
    sleep()
    if jwaring():
        data = "{'Lon':'119.467','Lat':'32.196','Switch':1,'Cycle':'6','Turn':1}"
        Data.objects.create(device_id=8, model=0, data=data, waring=1)


# jinger7
def jin7():
    sleep()
    if jwaring():
        data = "{'Lon':'119.465','Lat':'32.196','Switch':1,'Cycle':'6','Turn':0}"
        Data.objects.create(device_id=9, model=0, data=data, waring=1)


# detritus
def det1():
    sleep()
    if waring():
        data = "{'Lon':'119.4675','Lat':'32.1945','Switch':1,'Cycle':'6','Full':1}"
        Data.objects.create(device_id=12, model=0, data=data, waring=1)


def det2():
    sleep()
    if waring():
        data = "{'Lon':'119.4655','Lat':'32.19605','Switch':1,'Cycle':'6','Full':1}"
        Data.objects.create(device_id=33, model=0, data=data, waring=1)


def det3():
    sleep()
    if waring():
        data = "{'Lon':'119.4658','Lat':'32.1952','Switch':1,'Cycle':'6','Full':1}"
        Data.objects.create(device_id=14, model=0, data=data, waring=1)


thread = []

t1 = Thread(target=det1)
t2 = Thread(target=det2)
t3 = Thread(target=det3)
j1 = Thread(target=jin1)
j3 = Thread(target=jin3)
j6 = Thread(target=jin6)
j7 = Thread(target=jin7)
thread.append(t1)
thread.append(t2)
thread.append(t3)
thread.append(j1)
thread.append(j3)
thread.append(j6)
thread.append(j7)

for t in thread:
    t.start()
for t in thread:
    t.join()
