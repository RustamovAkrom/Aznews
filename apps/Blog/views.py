from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages
from django.urls import reverse

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Post, Categories, Tag, Comment
from .forms import SaveAnonimousUserEmailForm, WriteCommentForm, CreatePostForm
from apps.shared.models import Pictures


class BlogPage(View):

    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            posts = Post.objects.exclude(user = request.user).filter(is_active=True)
        else:
            posts = Post.objects.filter(is_active=True)

        categories = Categories.objects.all()
        tags = Tag.objects.all()
        form = SaveAnonimousUserEmailForm()
        
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
            if request.user.is_authenticated:
                response_categori = Post.objects.exclude(user = request.user).filter(categories = categories.get(name = categori))
            else:
                response_categori = Post.objects.filter(categories = categories.get(name = categori))

            context['posts'] = response_categori

        #searching in tags
        tag = request.GET.get('tag', None)
        if tag is not None:
            if request.user.is_authenticated:
                response_tag = Post.objects.exclude(user = request.user).filter(tags = tags.get(name = tag))
            else:
                response_tag = Post.objects.filter(tags = tags.get(name = tag))

            context['posts'] = response_tag

        return render(request, "blog/blog.html", context)
    
    def post(self, request):

        form = SaveAnonimousUserEmailForm(request.POST)

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

        form = SaveAnonimousUserEmailForm()
        comment_form = WriteCommentForm()

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

        form = SaveAnonimousUserEmailForm(request.POST)

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
        form = WriteCommentForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data.get("message")
            Comment.objects.create(post = post, user = request.user, message = message)
            messages.success(request, f"successfully sening message")
            return redirect(reverse("blog:blog"))
        
        else:
            messages.error(request, "Ow no your message are not valid !")
        return redirect(reverse("blog:blog-blog"))


class CreatePostPage(LoginRequiredMixin, View):
    
    def get(self, request):
        context = {}
        user_posts = Post.objects.filter(user = request.user)
        form = CreatePostForm()
        context['form'] = form
        context['user_posts'] = user_posts
        return render(request, "blog/create_post.html", context)

    def post(self, request):
        form = CreatePostForm(data=request.POST, files=request.FILES)
        print(form.data)
        if form.is_valid():
            post = Post.objects.create(
                user = request.user,
                title = form.cleaned_data.get("title"),
                descriptions = form.cleaned_data.get("descriptions"),
                content = form.cleaned_data.get("content"),
                categories = form.cleaned_data.get("categories"),
                tags = form.cleaned_data.get("tags"),
                content_image = form.cleaned_data.get("content_image"),
                is_active = form.cleaned_data.get("is_active")
            )
            messages.success(request, f"Successfully creted post ({post})")
            return redirect("blog:create-post")
        else:
            messages.error(request, "Your post are not valid !")
            return redirect("blog:create-post")


class UserPostsPage(LoginRequiredMixin, View):
    
    def get(self, request):
        context = {}
        return render(request, "blog/my_posts.html", context)


class PicturesPage(View):

    def get(self, request):
        context = {}
        pictures = Pictures.objects.all()

        page = request.GET.get('page', 1)
        size = request.GET.get('size', 12)

        pagination = Paginator(pictures, size)
        page_obj = pagination.page(page)
        context['page_obj'] = page_obj
        return render(request, "blog/pictures.html", context)