from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.NewsListView.as_view(), name='main_news'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('create/', views.NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/',views.NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/',views.NewsDeleteView.as_view(), name='news_delete'),
]

