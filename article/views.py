import re
from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all().order_by('-pk')
    return render(request, 'article/articles_list.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'article/article_detail.html', {'article': article})
