import re
from django.shortcuts import render


def dinner(request, menu, count):
    context = {
        'menu': menu,
        'count': count,
    }
    return render(request, 'pages/dinner.html', context)


def check(request):
    return render(request, 'pages/home.html')