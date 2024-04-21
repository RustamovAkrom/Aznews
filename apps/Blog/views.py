from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages
from django.urls import reverse

from .models import Post, Categories, Tag, Comment
from .forms import SaveAnonimousUserEmail, WriteComment
from apps.shared.models import Pictures


class BlogPage(View):

    def get(self, request):
        context = {}
        posts = Post.objects.filter(is_active=True)
        categories = Categories.objects.all()
        tags = Tag.objects.all()
        form = SaveAnonimousUserEmail()
        
        page = request.GET.get('page', 1)
        size = request.GET.get('size', 4)

        #Paginating
        pagination = Paginator(posts, size)
        page_obj = pagination.page(page)
        
        context['page_obj'] = page_obj
        context['posts'] = page_obj
        context['recent_posts'] = posts
        context['categories'] = categories
        context['tags'] = tags
        context['form'] = form

        #searching
        param = request.GET.get('q', None)
        if param is not None:
            response_param = Post.objects.filter(title__icontains = param)
            context['posts'] = response_param

        #searching in categories
        categori = request.GET.get('categoriy', None)
        if categori is not None:
            print(categori)
            response_categori = Post.objects.filter(categories = categories.get(name = categori))
            context['posts'] = response_categori

        #searching in tags
        tag = request.GET.get('tag', None)
        if tag is not None:
            response_tag = Post.objects.filter(tags = tags.get(name = tag))
            context['posts'] = response_tag

        return render(request, "blog/blog.html", context)
    
    def post(self, request):

        form = SaveAnonimousUserEmail(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You successfully saved email senk you")
            return redirect("blog:blog")
        else:
            messages.error(request, "It is email already token!")
            return redirect("blog:blog")


class BlogDetailPage(View):

    def get(self, request, pk):
        context = {}
        posts = Post.objects.all()
        categories = Categories.objects.all()
        tags = Tag.objects.all()
        post = posts.get(pk = pk)
        comments = Comment.objects.filter(post = post)

        form = SaveAnonimousUserEmail()
        comment_form = WriteComment()

        context['post'] = post
        context['comment_form'] = comment_form

        context['recent_posts'] = posts
        context['categories'] = categories
        context['tags'] = tags
        context['form'] = form
        context['comments'] = comments

        #searching
        param = request.GET.get('q', None)
        if param is not None:
            response_param = Post.objects.filter(title__icontains = param)
            context['posts'] = response_param

        #searching in categories
        categori = request.GET.get('categoriy', None)
        if categori is not None:
            print(categori)
            response_categori = Post.objects.filter(categories = categories.get(name = categori))
            context['posts'] = response_categori

        #searching in tags
        tag = request.GET.get('tag', None)
        if tag is not None:
            response_tag = Post.objects.filter(tags = tags.get(name = tag))
            context['posts'] = response_tag

        return render(request, "blog/single-blog.html", context)


    def post(self, request, pk):

        form = SaveAnonimousUserEmail(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You successfully saved email senk you")
            return redirect("blog:blog")
        else:
            messages.error(request, "It is email already token!")
            return redirect("blog:blog")
        

class BlogDetailLeaveReaply(View):

    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        form = WriteComment(request.POST)

        if form.is_valid():
            message = form.cleaned_data.get("message")
            Comment.objects.create(post = post, user = request.user, message = message)
            messages.success(request, f"successfully sening message")
            return redirect(reverse("blog:blog"))
        
        else:
            messages.error(request, "Ow no your message are not valid !")
        return redirect(reverse("blog:blog-blog"))

        
class PicturesPage(View):
    def get(self, request):
        pictures = Pictures.objects.all()
        return render(request, "blog/pictures.html", {"pictures": pictures})