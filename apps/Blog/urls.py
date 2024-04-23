from django.urls import path
from .views import BlogDetailPage, BlogPage, BlogDetailLeaveReaply, PicturesPage, CreatePostPage, UserPostsPage


app_name = "blog"
urlpatterns = [
    path("blog-home/", BlogPage.as_view(), name="blog"),
    path("blog-detail/<int:pk>", BlogDetailPage.as_view(), name="blog-detail"),
    path("blog-detail-comment-write/<int:pk>", BlogDetailLeaveReaply.as_view(), name="comment-write"),
    path("blog-pictures/", PicturesPage.as_view(), name="pictures"),
    path("blog-create-post/", CreatePostPage.as_view(), name="create-post"),
    path("blog-my-posts", UserPostsPage.as_view(), name="my-posts")
]