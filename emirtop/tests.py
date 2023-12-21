from django.test import TestCase

# Create your tests here.
# urls.py
from django.urls import path
from .views import current_time, portfolio

urlpatterns = [
    # ... Ваши существующие эндпоинты
    path('time/', current_time, name='current_time'),
    path('portfolio/', portfolio, name='portfolio'),
]
