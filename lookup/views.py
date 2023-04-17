#views.py file

from django.shortcuts import render
from . import views

def home(request):
	return render(request, 'home.html', {})
	
def about(request):
	return render(request, 'about.html', {})
	


