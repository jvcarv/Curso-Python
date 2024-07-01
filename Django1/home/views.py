from django.shortcuts import render
# Create your views here.


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/index.html', context)


def top(request):
    context = {
        'title': 'Top 3'
    }
    return render(request, 'home/top.html', context)


def gallery(request):
    context = {
        'title': 'Galeria'
    }
    return render(request, 'home/galeria.html', context)
