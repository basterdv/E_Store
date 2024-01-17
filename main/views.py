from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home'
    }
    return render(request, 'main/index.html',context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')
