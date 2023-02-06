from django.contrib import admin

from .models import User,Servicio,Pago

# Register your models here.

admin.site.register(User)
admin.site.register(Pago)
admin.site.register(Servicio)