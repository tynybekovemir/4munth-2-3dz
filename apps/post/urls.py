from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name="about-page"),
    path('contact/', contact, name="contact-page"),
    path('hi/', hello),
    path('bye/', goodbye),
    path('', index, name="index")
    
]