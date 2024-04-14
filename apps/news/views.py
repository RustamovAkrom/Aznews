from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


class HomePage(TemplateView):
    template_name = "news/index.html"


class CategoriPage(TemplateView):
    template_name = "news/categori.html"


class AboutPage(TemplateView):
    template_name = "news/about.html"


class LatesNewsPage(TemplateView):
    template_name = "news/latest_news.html"


class ContactPage(TemplateView):
    template_name = "news/contact.html"


class DetailsPage(TemplateView):
    template_name = "news/details.html"

