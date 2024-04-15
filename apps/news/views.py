from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from .models import News


class HomePage(View):
    def get(self, request):
        context = {}
        news = News.objects.all()
        new = News.objects.first()
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
        
        #follow us
        context['fans_facebook'] = 0
        context['fans_tweater'] = 0
        context['fans_instogram'] = 0
        context['fans_youtube'] = 0
        return render(request, 'news/index.html', context)


class CategoryPage(TemplateView):
    template_name = "news/categori.html"


class AboutPage(TemplateView):
    template_name = "news/about.html"


class LatestNewsPage(TemplateView):
    template_name = "news/latest_news.html"


class ContactPage(TemplateView):
    template_name = "news/contact.html"


class DetailsPage(View):
    def get(self, request, pk):
        detail_new = News.objects.get(pk = pk)
        return render(request, "news/details.html", {"detail_new": detail_new})
