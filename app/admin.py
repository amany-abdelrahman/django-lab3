from django.contrib import admin

# Register your models here.

from app.models import Student, my_users

admin.site.register(Student)

admin.site.register(my_users)