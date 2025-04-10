from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('<int:article_id>/', views.detail_article, name='detail_article'),
    path('<int:article_id>/commenter/', views.commenter_article, name='commenter_article'),
]
