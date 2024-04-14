from django.urls import path
from .views import HomePage, CategoriPage, AboutPage, LatesNewsPage, ContactPage, DetailsPage


app_name = "news"
urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("categori/", CategoriPage.as_view(), name="categori"),
    path("about/", AboutPage.as_view(), name="about"),
    path("lates-news/", LatesNewsPage.as_view(), name='lates-news'),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("details/",DetailsPage.as_view(), name="details"),
]