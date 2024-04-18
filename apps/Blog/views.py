from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Post


class BlogPage(View):
    def get(self, request):
        context = {}
        posts = Post.objects.filter(is_active=True)
        context['posts'] = posts
        return render(request, "blog/blog.html", context)

class BlogDetailPage(TemplateView):
    template_name = "blog/single-blog.html"

