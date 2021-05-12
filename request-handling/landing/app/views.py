from collections import Counter
from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')

    if from_landing == 'test':
        counter_click['test'] += 1
    elif from_landing == 'original':
        counter_click['original'] += 1

    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    template = request.GET.get('ab-test-arg')

    if template == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')
    else:
        counter_show['original'] += 1
        return render(request, 'landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_conversion = 0
    original_conversion = 0

    if counter_show['test'] != 0:
        test_conversion = round(counter_click['test'] / counter_show['test'], 1)

    if counter_show['original'] != 0:
        original_conversion = round(counter_click['original'] / counter_show['original'], 1)

    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
