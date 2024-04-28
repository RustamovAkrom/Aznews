from django.urls import path

from .views import (
    BlogDetailPage,
    BlogPage,
    BlogDetailLeaveReaply,
    PicturesPage,
    UserPostCreatePage,
    UserPostUpdatePage,
    UserPostDeletePage,
    UserPostsPage,
)


app_name = "blog"
urlpatterns = [
    path("blog-update-post/<int:pk>", UserPostUpdatePage.as_view(), name="update-post"),
    path("blog-delete-post/<int:pk>", UserPostDeletePage.as_view(), name="delete-post"),
    path("blog-detail/<int:pk>", BlogDetailPage.as_view(), name="blog-detail"),
    path("blog-create-post/", UserPostCreatePage.as_view(), name="create-post"),
    path("blog-home/", BlogPage.as_view(), name="blog"),
    path(
        "blog-detail-comment-write/<int:pk>",
        BlogDetailLeaveReaply.as_view(),
        name="comment-write",
    ),
    path("blog-pictures/", PicturesPage.as_view(), name="pictures"),
    path("blog-my-posts", UserPostsPage.as_view(), name="my-posts"),
]
