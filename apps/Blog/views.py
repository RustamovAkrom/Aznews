from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.views import View
from .models import Post


class BlogPage(View):
    def get(self, request):
        context = {}
        posts = Post.objects.filter(is_active=True)

        #Paginate 
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 4)
        pagination = Paginator(posts, size)
        page_obj = pagination.page(page)

        context['page_obj'] = page_obj
        context['posts'] = page_obj
        context['recent_posts'] = posts
        
        return render(request, "blog/blog.html", context)


class BlogDetailPage(View):
    def get(self, request, pk):
        context = {}
        post = Post.objects.get(pk = pk)
        context['post'] = post
        return render(request, "blog/single-blog.html", context)
    # template_name = "blog/single-blog.html"

