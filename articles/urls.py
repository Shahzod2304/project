from django.urls import path 
from .views import ArticleListView, ArticleDetailView, ArticleDeleteView
urlpatterns = [
    path('', ArticleListView.as_view(),name='article_list'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name="article_delete"),
    path('<int:pk>/',ArticleDetailView.as_view(),name='article_detail'),
]
