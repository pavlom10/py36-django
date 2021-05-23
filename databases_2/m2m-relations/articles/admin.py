from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # print(form.cleaned_data)
            if 'is_main' in form.cleaned_data and form.cleaned_data['is_main']:
                main_scopes += 1

        if main_scopes == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_scopes > 1:
            raise ValidationError('Основным может быть только 1 раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    ordering = ('-is_main',)
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleScopeInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
