from django.shortcuts import render
from .models import Station

def home(request):
    stations = Station.objects.all()

    return render(request, 'home.html', {'stations': stations})

def about(request):
    return render(request, 'about.html', {})