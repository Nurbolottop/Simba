from django.shortcuts import render
from apps.base import models

# Create your views here.
def index(request):
    slide = models.Slide.objects.all()
    
    return render(request, 'index-2.html', locals())
