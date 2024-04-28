from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import View
from django.contrib import messages
from django.urls import reverse


from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Post, Categories, Tag, Comment
from .forms import (
    SaveAnonimousUserEmailForm,
    WriteCommentForm,
    CreatePostForm,
    UpdatePostForm,
)

from apps.shared.models import Pictures


class BlogPage(View):

    def get(self, request):
        context = {}

        if request.user.is_authenticated:
            posts = Post.objects.exclude(user=request.user).filter(is_active=True)
        else:
            posts = Post.objects.filter(is_active=True)

        posts = posts.order_by("-created_at")

        categories = Categories.objects.all()
        tags = Tag.objects.all()
        form = SaveAnonimousUserEmailForm()

        page = request.GET.get("page", 1)
        size = request.GET.get("size", 4)

        # Paginating
        pagination = Paginator(posts, size)
        page_obj = pagination.page(page)

        context["page_obj"] = page_obj
        context["posts"] = page_obj
        context["recent_posts"] = posts
        context["categories"] = categories
        context["tags"] = tags
        context["form"] = form

        # searching
        param = request.GET.get("q", None)
        if param is not None:
            response_param = Post.objects.filter(title__icontains=param)
            context["posts"] = response_param

        # searching in categories
        categori = request.GET.get("categoriy", None)
        if categori is not None:
            if request.user.is_authenticated:
                response_categori = Post.objects.exclude(user=request.user).filter(
                    categories=categories.get(name=categori)
                )
            else:
                response_categori = Post.objects.filter(
                    categories=categories.get(name=categori)
                )

            context["posts"] = response_categori

        # searching in tags
        tag = request.GET.get("tag", None)
        if tag is not None:
            if request.user.is_authenticated:
                response_tag = Post.objects.exclude(user=request.user).filter(
                    tags=tags.get(name=tag)
                )
            else:
                response_tag = Post.objects.filter(tags=tags.get(name=tag))

            context["posts"] = response_tag

        # searching in user posts
        post_user_id = request.GET.get("user", None)
        if post_user_id is not None:
            posts = Post.objects.filter(user=post_user_id)
            return render(request, "blog/blog.html", {"posts": posts})

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
        post = posts.get(pk=pk)
        comments = Comment.objects.filter(post=post)

        form = SaveAnonimousUserEmailForm()
        comment_form = WriteCommentForm()

        context["post"] = post
        context["comment_form"] = comment_form

        if request.user.is_authenticated:
            context["recent_posts"] = (
                posts.exclude(id=post.id)
                .filter(user=request.user)
                .order_by("-created_at")
            )
        else:
            context["recent_posts"] = (
                posts.exclude(id=post.id)
                .filter(categories=post.categories)
                .order_by("-created_at")
            )

        context["categories"] = categories
        context["tags"] = tags
        context["form"] = form
        context["comments"] = comments

        # searching
        param = request.GET.get("q", None)
        if param is not None:
            response_param = Post.objects.filter(title__icontains=param)
            context["posts"] = response_param

        # searching in categories
        categori = request.GET.get("categoriy", None)
        if categori is not None:
            print(categori)
            response_categori = Post.objects.filter(
                categories=categories.get(name=categori)
            )
            context["posts"] = response_categori

        # searching in tags
        tag = request.GET.get("tag", None)
        if tag is not None:
            response_tag = Post.objects.filter(tags=tags.get(name=tag))
            context["posts"] = response_tag

        # searching in user posts
        post_user_id = request.GET.get("user", None)
        if post_user_id is not None:
            posts = Post.objects.filter(user=post_user_id)
            return render(request, "blog/blog.html", {"posts": posts})

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
        post = Post.objects.get(pk=pk)
        form = WriteCommentForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data.get("message")
            Comment.objects.create(post=post, user=request.user, message=message)
            messages.success(request, f"successfully sening message")
            return redirect(reverse("blog:blog"))

        else:
            messages.error(request, "Ow no your message are not valid !")
        return redirect(reverse("blog:blog-blog"))


class UserPostsPage(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        posts = Post.objects.all()
        categories = Categories.objects.all()
        tags = Tag.objects.all()

        page = request.GET.get("page", 1)
        size = request.GET.get("size", 4)

        # Paginating
        pagination = Paginator(posts.filter(user=request.user), size)
        page_obj = pagination.page(page)

        context["posts"] = page_obj
        context["page_obj"] = page_obj
        context["categories"] = categories
        context["recent_posts"] = posts.filter(user=request.user)
        context["tags"] = tags

        return render(request, "blog/my_posts.html", context)


class UserPostCreatePage(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        user_posts = Post.objects.filter(user=request.user)
        form = CreatePostForm()
        context["form"] = form
        context["user_posts"] = user_posts
        return render(request, "blog/create_post.html", context)

    def post(self, request):
        form = CreatePostForm(data=request.POST, files=request.FILES)
        print(form.data)
        if form.is_valid():
            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data.get("title"),
                descriptions=form.cleaned_data.get("descriptions"),
                content=form.cleaned_data.get("content"),
                categories=form.cleaned_data.get("categories"),
                tags=form.cleaned_data.get("tags"),
                content_image=form.cleaned_data.get("content_image"),
                is_active=form.cleaned_data.get("is_active"),
            )
            messages.success(request, f"Successfully creted post ({post})")
            return redirect("blog:create-post")
        else:
            messages.error(request, "Your post are not valid !")
            return redirect("blog:create-post")


class UserPostUpdatePage(LoginRequiredMixin, View):

    def get(self, request, pk):
        context = {}
        post = Post.objects.get(pk=pk)
        form = UpdatePostForm(instance=post)
        context["form"] = form
        context["post"] = post
        return render(request, "blog/update_post.html", context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = UpdatePostForm(data=request.POST, instance=post, files=request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, f"You successfully updated post ( {post.title} )")
            return redirect(reverse("blog:my-posts"))

        else:
            messages.error(request, "Pleace enter valid post configurations !")
            return redirect(reverse("blog:update-post", kwargs={"pk": post.pk}))


class UserPostDeletePage(LoginRequiredMixin, View):

    def get(self, request, pk):
        context = {}
        post = Post.objects.get(pk=pk)
        context["post"] = post
        return render(request, "blog/delete_post.html", context)

    def post(self, request, pk):

        post = Post.objects.get(pk=pk)
        post.delete()
        messages.success(request, "You are successfully deleted Post")
        return redirect(reverse("blog:my-posts"))


class PicturesPage(View):

    def get(self, request):
        context = {}
        pictures = Pictures.objects.all()

        page = request.GET.get("page", 1)
        size = request.GET.get("size", 12)

        pagination = Paginator(pictures, size)
        page_obj = pagination.page(page)
        context["page_obj"] = page_obj
        return render(request, "blog/pictures.html", context)
