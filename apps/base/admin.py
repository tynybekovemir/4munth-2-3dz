from django.contrib import admin
from .models import Settings, About, Course

# Register your models here.
admin.site.register(Settings)
admin.site.register(About)
admin.site.register(Course)
