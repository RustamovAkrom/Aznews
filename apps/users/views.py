from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate

from .forms import UserProfileForm, UserRegisterForm, UserLoginForm
from .models import User


class UserRegisterPage(TemplateView):
    def get(self, request):
        context = {}
        form = UserRegisterForm()
        context["form"] = form
        return render(request, "users/register.html", context)

    def post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Good you successfully registred, plreace enter username and password.",
            )
            return redirect("users:login")
        else:
            messages.error(request, "Ow no Bro. Your authentification are not valid !")
            return redirect("users:register")


class UserLoginPage(View):

    def get(self, request):
        context = {}
        form = UserLoginForm()
        context["form"] = form
        return render(request, "users/login.html", context)

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome the Aznews { username } ")
                return redirect("blog:blog")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("users:login")
        else:
            messages.warning(
                request, "Ow not Bro. Your username or password are not valid !"
            )
            return redirect("users:login")


class UserLogoutPage(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        return render(request, "users/logout.html", context)

    def post(self, request):
        logout(request)
        messages.success(request, "You successfully Logout")
        return redirect("blog:blog")


class UserProfilePage(LoginRequiredMixin, View):

    def get(self, request, pk):

        context = {}
        user = User.objects.get(pk=pk)
        form = UserProfileForm(instance=user)
        context["form"] = form
        return render(request, "users/profile.html", context)

    def post(self, request, pk):

        user = User.objects.get(pk=pk)
        form = UserProfileForm(data=request.POST, instance=user, files=request.FILES)

        if form.is_valid():

            form.save()
            messages.success(request, "your successfully updated profile")
            return redirect(reverse("users:profile", kwargs={"pk": user.pk}))

        else:
            messages.error(request, "Ow not Bro, you profile are not valid!")
            return redirect(reverse("users:profile", kwargs={"pk": user.pk}))
