from django.contrib import admin
from .models import ormapp, ormappAdmin
# Register your models here.
admin.site.register(ormapp, ormappAdmin)