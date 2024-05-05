from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all()
    # context = {'phones': phones_all}
    sort = request.GET.get('sort')
    queryset = super(phones_all).get_queryset().order_by('id')
    if sort == ('price'):
        context = queryset.order_by('price')
    if sort == ('-price'):
        context = queryset.order_by('-price')
    if sort == ('name'):
        context = queryset.order_by('name')
    if sort == ('-name'):
        context = queryset.order_by('-name')
    else:
        context = {'phones': phones_all}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = Phone.objects.filter(slug__contains=slug).first()
    return render(request, template, context)
