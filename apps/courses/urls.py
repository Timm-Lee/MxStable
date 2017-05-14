# -*- coding:utf-8 -*-
__author__ = 'TimLee'
__date__ = '5/14/17 8:43 AM'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView


urlpatterns = [

    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程详情首页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    # 课程开始学习
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),




]
