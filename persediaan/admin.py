from django.contrib import admin

# Register your models here.
from .models import Komponen
from .models import SubKomponen
from .models import Soalan

# Register your models here.
admin.site.register(Komponen)
admin.site.register(SubKomponen)
admin.site.register(Soalan)