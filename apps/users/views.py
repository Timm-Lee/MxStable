# coding:utf-8

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm
from operation.models import UserMessage
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin


class CustomBackend(ModelBackend):
    """
    自定义 authenticate 实现邮箱登录
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 查找用户是否存在
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 传入的密码，与 model 中的对比，只能用user.check_password
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    """
    用户登录
    """

    def get(self, request):
        return render(request, "login.html", {

        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {'msg': '用户未激活'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {
                'login_form': login_form
            })


class LogoutView(View):
    """
    用户登出
    """

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegisterView(View):
    """
    用户注册
    """

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {
            'register_form': register_form,
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'login.html', {'msg': '用户已存在'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()

            # 写入欢迎消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = u'欢迎注册慕学在线网'
            user_message.save()

            send_register_email(user_name, 'register')

            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {
                'register_form': register_form
            })


class ActiveUserView(View):
    """
    用户激活链接逻辑
    """
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')





