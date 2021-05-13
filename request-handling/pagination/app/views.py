from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv
from urllib.parse import urlencode

with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
    all_stations = list(csv.DictReader(csvfile))


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    PER_PAGE = 10

    paginator = Paginator(all_stations, PER_PAGE)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)

    next_page_url = reverse(bus_stations) + \
                    '?' + urlencode({'page': stations.next_page_number()}) if stations.has_next() else None
    prev_page_url = reverse(bus_stations) + \
                    '?' + urlencode({'page': stations.previous_page_number()}) if stations.has_previous() else None

    return render(request, 'index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
