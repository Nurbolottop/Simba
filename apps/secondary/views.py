from django.shortcuts import render
from apps.secondary.models import About
# Create your views here.
def about(request):
    about = About.objects.latest("id")
    return render(request, "about.html", locals())
