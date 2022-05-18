from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/news_main.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsCreateView(CreateView):
    model = News
    template_name = 'news/create_news.html'
    fields = '__all__'


class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'body']
    template_name = 'news/news_edit.html'


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('main_news')


# Create your views here.
