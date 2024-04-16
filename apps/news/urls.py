from django.urls import path
from .views import HomePage, CategoryPage, AboutPage, LatestNewsPage, ContactPage, DetailsPage


app_name = "news"
urlpatterns = [
    path("details/<int:pk>", DetailsPage.as_view(), name = "details"),
    path("", HomePage.as_view(), name="home"),
    path("category/", CategoryPage.as_view(), name="category"),
    path("about/", AboutPage.as_view(), name="about"),
    path("latest-news/", LatestNewsPage.as_view(), name='latest-news'),
    path("contact/", ContactPage.as_view(), name="contact"),
]