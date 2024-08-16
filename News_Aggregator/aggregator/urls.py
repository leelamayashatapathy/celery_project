# news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('latest-news/', views.latest_news, name='latest_news'),
]
