from django.urls import path
from .views import UserRegisterPage, UserLoginPage, UserLogoutPage


app_name = "users"
urlpatterns = [
    path("register/", UserRegisterPage.as_view(), name="register"),
    path("login/", UserLoginPage.as_view(), name="login"),
    path("logout/", UserLogoutPage.as_view(), name="logout")
]