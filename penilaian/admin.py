from django.contrib import admin

# Register your models here.
from .models import Sesi,Jadual

admin.site.register(Sesi)
admin.site.register(Jadual)