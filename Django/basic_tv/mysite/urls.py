# urls.py 를 생성 => include 할 경우, 꼭 urlapatterns = [] 를 작성하자.

from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    # /mysite/
    path('', views.home),
    # /mysite/lunch/
    path('lunch/', views.lunch, name='lunch'),
    # /mysite/lotto/
    path('lotto/', views.lotto, name='lotto'),
    # /mysite/greeting/<var>/ <= Variable Routing
    path('greeting/<str:name>/', views.greeting)
]
