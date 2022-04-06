from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # Create
    # articles/new/
    path('new/', views.new, name='new'),
    # articles/create/
    path('create/', views.create, name='create'),

    # Read
    # articles/
    path('', views.list, name='list'),
    # articles/1/
    path('<int:pk>/', views.detail, name='detail'),

    # Update
    # articles/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # articles/1/update/
    path('<int:pk>/update/', views.update, name='update'),

    # Delete
    # articles/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
]
