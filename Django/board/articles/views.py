from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article

"""
1. 글 작성 버튼을 누르면(/aritcles/new)
2. form 제공
3. form 제출시 (/articles/create)
4. 글 작성(db save)
5. detail 페이지로 이동 / list 이동
"""

# Create
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()

    # 현재 요청보낸 브라우저의 url을 /articles/3/로 바꿔주세요
    return redirect('articles:detail', article.pk)


# Read
def list(request):
    # id 오름차순이 기본값
    # articles = Article.objects.all()

    # id 내림차순 (python)
    # articles = Article.objects.all()[::-1]

    # id 내림차순 (ORM)
    # articles = Article.objects.order_by('-pk')

    # updated_at 내림차순
    articles = Article.objects.order_by('-updated_at')
    context = {'articles': articles, }
    return render(request, 'articles/list.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article, }
    return render(request, 'articles/detail.html', context)


# Update
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article, }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return redirect('articles:detail', article.pk)


# Delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:list')
    elif request.method == 'GET':
        return redirect('articles:detail', article.pk)

