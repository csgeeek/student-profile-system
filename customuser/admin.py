from django.contrib import admin

from .models import CustomUser, College, Student
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(College)
admin.site.register(Student)