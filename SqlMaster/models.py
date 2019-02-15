from django.db import models


# Create your models here.

class Domain(models.Model):
    name = models.CharField(max_length=30, verbose_name="域名", null=False, unique=True)
    city = models.CharField(max_length=10, verbose_name="城市", null=False)
    province = models.CharField(max_length=10, verbose_name="省份", null=True)
    country = models.CharField(max_length=10, verbose_name="国家", null=True, default="中国")
    date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    username = models.CharField(max_length=15, verbose_name="用户名", null=False, db_index=True)
    password = models.CharField(max_length=40, verbose_name="密码", null=False)
    name = models.CharField(max_length=12, verbose_name="昵称", null=False)
    domain = models.ForeignKey("Domain", verbose_name="所属域", on_delete=models.CASCADE, related_name="users")
    system = models.ManyToManyField("System", verbose_name="子系统", related_name="admin")
    phone = models.CharField(max_length=14, verbose_name="手机号", null=False, unique=True)
    email = models.EmailField(verbose_name="邮箱", null=False, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name="年龄", null=True)
    sex = models.NullBooleanField(verbose_name="性别", null=True)
    date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    rely = models.ForeignKey("Users", verbose_name="上级用户", null=True, on_delete=models.CASCADE, related_name="sub_user")

    def __str__(self):
        return self.username


class System(models.Model):
    name = models.CharField(max_length=10, verbose_name="系统名称", null=False)
    platform = models.CharField(max_length=8, verbose_name="系统平台", null=False, default="Others")
    createuser = models.ForeignKey("Users", verbose_name="创建者", on_delete=models.SET_NULL, null=True,
                                   related_name="ownsystem" , db_index=True)
    protocol = models.CharField(max_length=4, verbose_name="接入协议", default="CoAP")
    devicecode = models.CharField(max_length=20, verbose_name="设备注册码", null=True)
    domain = models.ForeignKey("Domain", verbose_name="所属域", on_delete=models.CASCADE, related_name="system")
    # JSON格式的数据模板，使用元组格式；
    type = models.CharField(max_length=300, verbose_name="数据模板", null=False)
    date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=30, verbose_name="设备名", null=False)
    system = models.ForeignKey("System", verbose_name="所属系统", on_delete=models.CASCADE, related_name="device")
    date = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    IMEI = models.CharField(max_length=15, verbose_name="序列号", null=False)

    def __str__(self):
        return self.name


class Data(models.Model):
    device = models.ForeignKey("Device", verbose_name="所属设备", on_delete=models.CASCADE, related_name="data")
    # JSON格式数据存储，采用字典（JS中的对象）格式；
    data = models.CharField(max_length=600, verbose_name="设备数据", null=False)
    date = models.DateTimeField(verbose_name="接收时间", auto_now_add=True)
    model = models.BooleanField(verbose_name="订阅/推送", default=0, db_index=True)
    # 0:订阅(pull) 1:推送(push)
    waring = models.NullBooleanField(verbose_name="正常/异常", default=None, null=True, db_index=True)
    # null:正常 0:解除异常 1:异常

    def __str__(self):
        return self.data


class Login(models.Model):
    user = models.ForeignKey("Users", verbose_name="用户", on_delete=models.CASCADE, related_name="login")
    IP = models.GenericIPAddressField(verbose_name="IP")
    operation = models.CharField(max_length=3, verbose_name="操作", null=False, default='IN')
    date = models.DateTimeField(verbose_name="时间", auto_now_add=True)

    def __str__(self):
        return self.user.name


class Operation(models.Model):
    code = models.PositiveSmallIntegerField(verbose_name="操作码", null=False)
    date = models.DateTimeField(verbose_name="操作时间", auto_now_add=True)
    user = models.ForeignKey("Users", verbose_name="操作用户", on_delete=models.CASCADE, related_name="operation")

    def __str__(self):
        return self.code

    '''
    operation_code = {
    900:"创建域",
    100:"修改域",
    101:"创建用户",
    102:"删除用户",
    103:"修改用户",
    202:"增加系统",
    203:"删除系统",
    204:"修改系统",
    205:"系统权限",
    302:"增加设备",
    303:"删除设备",
    304:"修改设备"，
    305:"命令推送"，
    401:"异常处理",    
    500:"无效操作",
    }
    '''
