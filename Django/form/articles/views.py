from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from .forms import ArticleForm


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():  # <= 실패시 form에 에러메시지가 담김
            article = form.save()
            return redirect('articles:detail', article.pk)
    elif request.method == 'GET':
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/new.html', context)


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)


def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
