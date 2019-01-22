from django.contrib import admin

# Register your models here.
from django.contrib import admin
from SqlMaster.models import Domain, Users, System, Device, Data, Login, Operation

admin.site.register(Domain)
admin.site.register(Users)
admin.site.register(System)
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(Login)
admin.site.register(Operation)
