# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Course

# Create your views here.


class CourseListView(View):
    """
    课程列表页
    """
    def get(self, request):
        all_courses = Course.objects.all()
        hot_courses = all_courses.order_by("-click_nums")[:3]

        sort = request.GET.get('sort', '')

        paginator = Paginator(all_courses, 6)
        page = request.GET.get('page', 1)

        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)



        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
        })


class CourseDetailView(View):
    """
    课程详情首页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        return render(request, 'course-detail.html', {
            'course': course,

        })


class CourseInfoView(View):
    """
    开始学习
    """
    def get(self, request, course_id):

        return render(request, 'course-video.html', {

        })







