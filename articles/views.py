from django.views.generic import ListView, DetailView
from . models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'