from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def current_time(request):
    current_time = datetime.datetime.now()
    return render(request, 'time.html', {'current_time': current_time})

def portfolio(request):
    # Здесь можете добавить логику для отображения вашего портфеля
    return render(request, 'portfolio.html')
