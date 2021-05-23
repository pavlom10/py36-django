from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=50, verbose_name='Раздел')
    articles = models.ManyToManyField(Article, related_name='scopes', through='ArticleScope')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, verbose_name='Раздел', on_delete=models.CASCADE)
    is_main = models.BooleanField(null=False, default=False, verbose_name='Основной')

    class Meta:
        verbose_name_plural = 'Тематики статьи'

    # def __str__(self):
    #     return '{0}_{1}'.format(self.article, self.scope)

