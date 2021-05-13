from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(settings.INFLATION_CSV, newline='') as csvfile:
        inflation = list(csv.reader(csvfile, delimiter=';'))

    context = {'inflation': inflation}

    return render(request, template_name,
                  context)