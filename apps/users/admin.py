# -*- coding:utf-8 -*-
from django.contrib import admin

from .models import EmailVerifyRecord, Banner, UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'nick_name', 'mobile', 'gender', 'address']
    search_fields = ['username', 'email', 'nick_name', 'mobile', 'gender', 'address']
    list_filter = ['username', 'email', 'nick_name', 'mobile', 'gender', 'address']


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-address-book-o'


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
admin.site.register(Banner, BannerAdmin)