from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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
    quote = get_object_or_404(Quote, pk = quote_id)
    context = {
        'quote' : quote
    }
    return render(request, 'quotes/detail.html', context)

def search(request):
    return render(request, 'quotes/search.html')

def create(request):
    return render(request, 'quotes/create.html')

def update(request):
    return render(request, 'quotes/update.html')

def delete(request, quote_id):
    quote = get_object_or_404(Quote, pk = quote_id)
    quote.delete()
    return redirect('quotes:search')