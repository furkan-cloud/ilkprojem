from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import Http404
from .models import Quote
from .forms import QuoteForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.

def index(request):
    quotes = Quote.objects.all()
    context = {
        'quotes' : quotes
    }
    return render(request, 'quotes/list.html', context)

def detail(request, slug):
    quote = get_object_or_404(Quote, slug = slug)
    
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.quote = quote
        comment.save()
        return HttpResponseRedirect(quote.get_absolute_url())
    
    context = {
        'quote' : quote,
        'form' : form,
    }
    return render(request, 'quotes/detail.html', context)

def search(request):
    return render(request, 'quotes/search.html')

def create(request):
    if not request.user.is_authenticated:
        raise Http404

    form = QuoteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        quote = form.save(commit=False)
        quote.user = request.user
        quote.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(quote.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'quotes/form.html', context)

def update(request, slug):
    if not request.user.is_authenticated:
        raise Http404
    quote = get_object_or_404(Quote, slug = slug)
    form = QuoteForm(request.POST or None, request.FILES or None, instance=quote)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz')
        return HttpResponseRedirect(quote.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'quotes/form.html', context)


def delete(request, slug):
    if not request.user.is_authenticated:
        raise Http404
    quote = get_object_or_404(Quote, slug = slug)
    quote.delete()
    return redirect('/quotes')