from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello Geeks")

def goodbye(request):
    return HttpResponse("Goood Bye")

def index(request):
    context = {
        'title': "Главная страница",
        'description': "Geeks",
        'greetings': "Добро пожаловть!",
        'benefits': ["это Geeks", "Удобный коворкинг", "Отличные преподователи", "Бесплатные ноутбуки"]
    }
    return render(request, 'post/index.html', context)


def about(request):
    context = {
        'title': "О нас",
        'description': "О нас",
        'greetings': "Добро пожаловть!",
        'numbers': ['200+ студентов', '70+ менторов', '50+ выпускников', '5+ филиалов']
    }
    return render(request, 'post/about.html', context)

def contact(request):
    zapros = {
        'title': "Контакты",
        'description': "Свяжитесь с нами",
        'phone': "0771244745",
        'instagram': "https://www.instagram.com/_abdykadyrov_s/",
        'telegram': "https://t.me/Abdykadyrov_S"
    }
    return render(request, 'post/contact.html', zapros)

