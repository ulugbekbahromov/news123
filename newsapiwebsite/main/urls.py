from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("bbc-news", views.bbc_news, name="bbc-news"),
    path("reuters", views.reuters, name="reuters"),
    path("nbcnews", views.nbc_news, name="nbc-news"),
    path("abcnews", views.abc_news, name="abc-news"),
    path("cnnnews", views.cnn_news, name="cnn-news"),
    path("politico", views.politico, name="politico"),
    path("techcrunch", views.tech_crunch, name="tech_crunch"),
    path("zen-today-history", views.zen_today_history, name="zen-today-history"),
    path("zen-quotes", views.zen_quotes, name="zen-quotes")
]