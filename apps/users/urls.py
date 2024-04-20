from django.urls import path
from .views import UserRegisterPage, UserLoginPage, UserLogoutPage, UserProfilePage, CreatePostPage


app_name = "users"
urlpatterns = [
    path("register/", UserRegisterPage.as_view(), name="register"),
    path("login/", UserLoginPage.as_view(), name="login"),
    path("logout/", UserLogoutPage.as_view(), name="logout"),
    path("profile/<int:pk>", UserProfilePage.as_view(), name="profile"),
    path("create-post/", CreatePostPage.as_view(), name="create-post")
]