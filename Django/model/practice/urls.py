from django.urls import path
from . import views

app_name = 'practice'

# /articles/ 
urlpatterns = [
    # /articles/ => article list (전체 목록)
    path('', views.article_list, name='article_list'),
    # /articles/1/ => 해당 pk값을 갖는 article detail
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
]
