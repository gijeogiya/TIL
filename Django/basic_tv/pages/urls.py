# pages.urls.py

from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # /pages/dinner/chicken/6/
    path('dinner/<str:menu>/<int:count>/', views.dinner),
    # /pages/check/
    path('check/', views.check, name='lotto')
]