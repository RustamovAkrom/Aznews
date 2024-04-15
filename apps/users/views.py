from django.shortcuts import render
from django.views.generic import TemplateView


class UserRegisterPage(TemplateView):
    template_name = "users/register.html"


class UserLogoutPage(TemplateView):
    template_name = "users/logout.html"


class UserLoginPage(TemplateView):
    template_name = "users/login.html"