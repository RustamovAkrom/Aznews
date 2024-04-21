from django.urls import path
from .views import BlogDetailPage, BlogPage, BlogDetailLeaveReaply, PicturesPage


app_name = "blog"
urlpatterns = [
    path("blog-home/", BlogPage.as_view(), name="blog"),
    path("blog-detail/<int:pk>", BlogDetailPage.as_view(), name="blog-detail"),
    path("blog-detail-comment-write/<int:pk>", BlogDetailLeaveReaply.as_view(), name="comment-write"),
    path("blog-pictures/", PicturesPage.as_view(), name="pictures"),
]