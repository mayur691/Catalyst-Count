from django.contrib import admin

# Register your models here.

from .models import Employee,Upload

admin.site.register(Employee)
admin.site.register(Upload)