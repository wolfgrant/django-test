from django.shortcuts import render

from .models import Demo

# Create your views here.

def index(request):

    template = "main/index.html"

    context= {
        "trips": Demo.objects.all()
    }

    return render(request, template, context)