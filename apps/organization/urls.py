# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/13/17 7:27 AM'

from django.conf.urls import url
from .views import OrgView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),




]