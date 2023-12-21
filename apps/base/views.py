from django.shortcuts import render
from .models import Settings, About, Course

# Create your views here.
def index(request):
    title = "Geeks"
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    courses = Course.objects.all().order_by("?")[:4]
    return render(request, 'index.html', locals())