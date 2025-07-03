from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
]