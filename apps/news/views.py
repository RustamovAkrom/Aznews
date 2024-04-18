from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView, DetailView, TemplateView
from django.views import View

from django.core.paginator import Paginator

from django.contrib import messages
from config.celery import app

from django.core.mail import send_mail
from dotenv import load_dotenv
load_dotenv()

from .models import News, Catgoriyes
from .forms import DetailsContactForm
from apps.shared.models import YouTubeVideoUrl

import os

class HomePage(View):
    def get(self, request):
        context = {}
        news = News.objects.filter(is_active=True)
        new = News.objects.first()

        videos = [str(i.url).strip('https://youtu.be/') for i in YouTubeVideoUrl.objects.all()]

        # . . . 
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 4)
        #Paginate pages
        pagination = Paginator(news.order_by('id'), size)
        page_obj = pagination.page(page)
        context['page_obj'] = page_obj

        context['tranding_top'] = new
        context['trending_buttom'] = page_obj
        context['right_content'] = page_obj
        context['weekly_top_news'] = news

        #follow us
        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0 

        #all
        context['card_one'] = page_obj
        #life & style 
        context['card_two'] = news.filter(categories=2)
        #travel
        context['card_three'] = news.filter(categories=1)
        #fashion
        context['card_fure'] = news.filter(categories=3)
        #sports
        context['card_five'] = news.filter(categories=4)
        #technologiy
        context['card_six'] = news.filter(categories=5)
        #articles
        context['recent_articles'] = news
        #youtube videos
        context['youtube_videos'] = videos

        #searching
        param = request.GET.get('q', None)
        if param is not None:
            response_param = news.filter(title__icontains = param)
            if response_param:
                context['tranding_top'] = response_param[0]
                context['right_content'] = response_param[1:]
                context['trending_buttom'] = response_param[1:]

        return render(request, 'news/index.html', context)


class CategoryPage(View):
    def get(self, request):
        context = {}
        news = News.objects.filter(is_active=True)
 # . . . 
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 4)
        #Paginate pages
        pagination = Paginator(news.order_by('id'), size)
        page_obj = pagination.page(page)
        context['page_obj'] = page_obj

        #all
        context['card_one'] = page_obj
        #life & style 
        context['card_two'] = news.filter(categories=2)
        #travel
        context['card_three'] = news.filter(categories=1)
        #fashion
        context['card_fure'] = news.filter(categories=3)
        #sports
        context['card_five'] = news.filter(categories=4)
        #technologiy
        context['card_six'] = news.filter(categories=5)

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