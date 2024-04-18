from django.shortcuts import render
from django.views.generic import TemplateView


class BlogPage(TemplateView):
    template_name = "blog/blog.html"


class BlogDetailPage(TemplateView):
    template_name = "blog/single-blog.html"

