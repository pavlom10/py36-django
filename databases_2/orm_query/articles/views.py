from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.all()\
        .select_related('author', 'genre')\
        .only('title', 'text', 'image', 'author', 'genre')\
        .order_by(ordering)

    context['articles'] = articles

    return render(request, template_name, context)
