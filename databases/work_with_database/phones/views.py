from django.shortcuts import render
from django.shortcuts import get_object_or_404
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {}

    phones_query = Phone.objects.all()

    sort_filter = request.GET.get('sort')
    if sort_filter:
        if sort_filter == 'name':
            phones_query = phones_query.order_by('name')
        elif sort_filter == 'min_price':
            phones_query = phones_query.order_by('price')
        elif sort_filter == 'max_price':
            phones_query = phones_query.order_by('-price')

    context['phones'] = phones_query
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}

    phone = get_object_or_404(Phone, slug=slug)
    context['phone'] = phone

    return render(request, template, context)
