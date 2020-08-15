from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import Http404
from .models import Quote
from .forms import QuoteForm
from django.contrib import messages

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
    form = QuoteForm(request.POST or None)
    if form.is_valid():
        quote = form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(quote.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'quotes/form.html', context)

def update(request, quote_id):
    quote = get_object_or_404(Quote, pk = quote_id)
    form = QuoteForm(request.POST or None, instance=quote)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(quote.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'quotes/form.html', context)


def delete(request, quote_id):
    quote = get_object_or_404(Quote, pk = quote_id)
    quote.delete()
    return redirect('/quotes')