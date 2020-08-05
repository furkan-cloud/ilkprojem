from django.shortcuts import render
from django.http import Http404
from .models import Quote

# Create your views here.

def index(request):
    quotes = Quote.objects.all()
    context = {
        'quotes' : quotes
    }
    return render(request, 'quotes/list.html', context)

def detail(request, quote_id):
    try:
        quote = Quote.objects.get(pk = quote_id)
    except Quote.DoesNotExist:
        raise Http404('Aradaığınız kayıt yok')
    return render(request, 'quotes/detail.html', quote)

def search(request):
    return render(request, 'quotes/search.html')