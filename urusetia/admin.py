from django.contrib import admin

# Register your models here.
from .models import Bahagian
from .models import Zon

# Register your models here.
admin.site.register(Bahagian)
admin.site.register(Zon)