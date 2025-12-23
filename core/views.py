from django.shortcuts import render

def index_views(request):
    return render(request, 'index.html', {})

def cars_views(request):
    return render(request, 'cars.html', {})

def ret(request):
    return render(request, 'ret.html', {})