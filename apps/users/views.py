from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .forms import UserProfileForm
from .models import User
from django.contrib import messages
from django.urls import reverse



class UserRegisterPage(TemplateView):
    template_name = "users/register.html"


class UserLogoutPage(TemplateView):
    template_name = "users/logout.html"


class UserLoginPage(TemplateView):
    template_name = "users/login.html"


class UserProfilePage(View):

    def get(self, request, pk):
        context = {}
        user = User.objects.get(pk = pk)
        form = UserProfileForm(instance = user)
        context['form'] = form
        return render(request, "users/profile.html", context)
    
    def post(self, request, pk):
        user = User.objects.get(pk = pk)
        form = UserProfileForm(data=request.POST, instance = user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "your successfully updated")
            return redirect(reverse("users:profile", kwargs={"pk":user.pk}))
        
        else:
            messages.error(request, "Ow not Bro, you profile are not valid!")
            return redirect(reverse("users:profile", kwargs={"pk":user.pk}))
        

class CreatePostPage(TemplateView):
    template_name  ="users/create_post.html"