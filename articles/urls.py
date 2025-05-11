from django.urls import path
from articles import views 

urlpatterns = [
    path('articles/<int:article_id>', views.articles_req, name='articles'),
]