from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleScope


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    ordering = '-published_at'
    articles = Article.objects.all().order_by(ordering).prefetch_related(
        'scopes', 'articlescope_set'
    )

    for article in articles:
        try:
            article_scope = article.articlescope_set.get(is_main=True)
            article.main_scope_id = article_scope.scope.id
        except ArticleScope.DoesNotExist:
            pass

    context['object_list'] = articles

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, template, context)
