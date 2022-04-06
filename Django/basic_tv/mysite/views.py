from django.shortcuts import render  # => HTML 을 응답으로 주는 함수
from django.http import HttpResponse # => 그냥 데이터를 응답으로 주는 함수
import random


def home(request):
    # HTML 파일은 기본적으로 INSTALLED_APPS > templates 에서 찾는다!
    return render(request, 'mysite/home.html')


def lunch(request):
    # menus 중 랜덤한 하나의 메뉴를 보여주자!
    menus = ['설렁탕', '곱창', '회', '똠양꿍', ]
    menu = random.choice(menus)
    context = {
        'menu': menu,
    }
    return render(request, 'mysite/lunch.html', context)


def lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    context = {
        'lucky_numbers': lucky_numbers,
    }
    return render(request, 'mysite/lotto.html', context)


def greeting(request, name):
    context = {
        'name': name.capitalize(),
    }
    return render(request, 'mysite/greeting.html', context)
