# -*- coding:utf-8 -*-
"""MxStable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from MxStable.settings import MEDIA_ROOT
from django.views.generic import TemplateView

from users.views import LoginView, LogoutView, RegisterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 处理 media 的访问，用于图片获取
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 首页
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    # 登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 用户登出
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

    # 用户注册
    url(r'^register/$', RegisterView.as_view(), name='register'),

    # 验证码图片的路由
    url(r'^captcha/', include('captcha.urls')),


]



