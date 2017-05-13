# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/13/17 7:27 AM'

from django.conf.urls import url
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView


urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),

    # 用户咨询课程 （Ajax）
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),

    # 机构详情首页
    url(r'^home/(?P<org_id>.*)/$', OrgHomeView.as_view(), name="org_home"),

    # 机构课程列表首页
    url(r'^course/(?P<org_id>.*)/$', OrgCourseView.as_view(), name="org_course"),

    # 机构介绍页
    url(r'^desc/(?P<org_id>.*)/$', OrgDescView.as_view(), name="org_desc"),

    # 机构讲师页
    url(r'^org_teacher/(?P<org_id>.*)/$', OrgTeacherView.as_view(), name="org_teacher"),

    # 机构收藏功能（Ajax）
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),




]
