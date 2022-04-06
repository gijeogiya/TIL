from django.shortcuts import render
from .models import Article


def article_list(request):
    # DB의 모든 Article 목록 조회
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'practice/article_list.html', context)


def article_detail(request, article_pk):
    # DB의 pk=article_pk 인 Article 조회
    article = Article.objects.get(pk=article_pk)

    context = {
        'article': article,
    }
    return render(request, 'practice/article_detail.html', context)