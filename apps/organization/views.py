# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import CourseOrg, CityDict, Teacher


# Create your views here.

class OrgView(View):
    """
        课程机构列表功能
        """

    def get(self, request):
        # 获得所有机构
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        # 获得所有城市
        all_citys = CityDict.objects.all()

        # 关键词机构搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))

        # 城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_orgs = all_orgs.order_by("-students")
        elif sort == 'courses':
            all_orgs = all_orgs.order_by("-course_nums")

        paginator = Paginator(all_orgs, 5)
        page = request.GET.get('page', 1)

        try:
            orgs = paginator.page(page)
        except PageNotAnInteger:
            orgs = paginator.page(1)
        except EmptyPage:
            orgs = paginator.page(paginator.num_pages)

        org_nums = all_orgs.count()

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort,

        })




