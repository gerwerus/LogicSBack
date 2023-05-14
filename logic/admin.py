from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

class CustomUserAdmin(UserAdmin):
    model = StudentUser
    list_display = ['email', 'username',]

admin.site.register(StudentUser, CustomUserAdmin)