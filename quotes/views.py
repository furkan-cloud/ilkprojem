from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'quotes/list.html')

def detail(request):
    return render(request, 'quotes/detail.html')

def search(request):
    return render(request, 'quotes/search.html')