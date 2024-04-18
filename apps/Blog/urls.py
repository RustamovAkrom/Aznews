from django.urls import path
from .views import BlogDetailPage, BlogPage


app_name = "blog"
urlpatterns = [
    path("blog-home/", BlogPage.as_view(), name="blog"),
    path("blog-detail/<pk>", BlogDetailPage.as_view(), name="blog-detail")
]