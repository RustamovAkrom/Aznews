from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from .models import News
from .forms import DetailsContactForm
from apps.shared.models import YouTubeVideoUrl
from django.contrib import messages
from config.celery import app

from django.core.mail import send_mail
from dotenv import load_dotenv
load_dotenv()

import os

class HomePage(View):
    def get(self, request):
        context = {}
        news = News.objects.filter(is_active=True)
        new = News.objects.first()

        videos = [str(i.url).strip('https://youtu.be/') for i in YouTubeVideoUrl.objects.all()]

        context['tranding_top'] = new
        context['trending_buttom'] = news
        context['right_content'] = news
        context['weekly_top_news'] = news

        context['card_one'] = news
        context['card_two'] = news
        context['card_three'] = news
        context['card_fure'] = news
        context['card_five'] = news
        context['card_six'] = news
        context['recent_articles'] = news

        context['youtube_videos'] = videos
        
        #follow us
        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0
        return render(request, 'news/index.html', context)


class CategoryPage(View):
    def get(self, request):
        context = {}
        news = News.objects.filter(is_active=True)

        context['card_one'] = news
        context['card_two'] = news
        context['card_three'] = news
        context['card_fure'] = news
        context['card_five'] = news
        context['card_six'] = news

        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0

        return render(request, "news/categori.html", context)
    

class AboutPage(View):
    def get(self, request):
        context = {}

        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0

        return render(request, "news/about.html", context)
    # template_name = "news/about.html"


class LatestNewsPage(View):
    def get(self, request):
        context = {}
        news = News.objects.filter(is_active=True)
        new = news.first()
        videos = [str(i.url).strip('https://youtu.be/') for i in YouTubeVideoUrl.objects.all()]
        form = DetailsContactForm()

        context['form'] = form
        context['tranding_top'] = new
        #follow us
        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0

        context['youtube_videos'] = videos
        return render(request, "news/latest_news.html", context)

    def post(self, request):
        form = DetailsContactForm(request.POST)
        if form.is_valid():

            message = form.cleaned_data.get('message')
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            
            app.task()
            send_mail(from_email = os.getenv("EMAIL_HOST_USER"), 
                      subject = subject, 
                      message = message, 
                      recipient_list = [email])
            
            print(message, name, email, subject)
            messages.success(request, "You succesfully sending")
            return redirect(reverse("news:latest-news"))
        
        else:
            messages.error(request, "Your sending is are not valid!")
            return redirect("news:latest-news")
        

class ContactPage(View):
    def get(self, request):
        context = {}
        context['form'] = DetailsContactForm()
        return render(request, "news/contact.html", context)
    
    def post(self, request):
        form = DetailsContactForm(request.POST)
        if form.is_valid():
            
            message = form.cleaned_data.get('message')
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            
            app.task()
            send_mail(from_email = os.getenv("EMAIL_HOST_USER"), 
                      subject = subject, 
                      message = f"{name} :{message}", 
                      recipient_list = [email])

            messages.success(request, "You succesfully sending")
            return redirect(reverse("news:contact"))
        
        else:
            messages.error(request, "Your sending is are not valid!")
            return redirect("news:contact")
        
        
class DetailsPage(View):
    def get(self, request, pk):
        context = {}
        detail_new = News.objects.get(pk = pk)
        form = DetailsContactForm()

        context['detail_new'] = detail_new
        context['form'] = form

        #follow us
        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0

        return render(request, "news/details.html", context)

    def post(self, request, pk):
        form = DetailsContactForm(request.POST)
        if form.is_valid():

            message = form.cleaned_data.get('message')
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            subject = form.cleaned_data.get("subject")
            
            app.task()
            send_mail(from_email = os.getenv("EMAIL_HOST_USER"), 
                      subject = subject, 
                      message = f"{name} :{message}", 
                      recipient_list = [email])
            
            messages.success(request, "You succesfully sending")
            return redirect(reverse("news:details", kwargs={"pk":pk}))
        
        else:
            messages.error(request, "Your sending is are not valid!")
            return redirect("news:details", kwargs={"pk":pk})