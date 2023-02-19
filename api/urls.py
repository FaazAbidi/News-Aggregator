from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/favourite/', views.favourite, name='favourite'),
]