from django.views.generic import ListView,DetailView
from .models import Article
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
    model= Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')