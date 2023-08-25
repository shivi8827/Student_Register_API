
from django.contrib import admin
from .models import Class, CustomUser

# Register your models here.
admin.site.register(Class)

admin.site.register(CustomUser)

# from django.contrib.auth.admin import UserAdmin
# #from .models import User

# def activate_users(modeladmin, request, queryset):
#     queryset.update(status='active')

# def deactivate_users(modeladmin, request, queryset):
#     queryset.update(status='inactive')

# class CustomUserAdmin(UserAdmin):
    
#     action = 
#     ordering = ('phone',)

# admin.site.register(CustomUser, CustomUserAdmin)