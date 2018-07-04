
from django.shortcuts import render
from .models import Bahagian

# Create your views here.

def home(request):
	return render(request,'base.html')

def index(request):
	return render(request,'dashboard.html')

def user(request):
	return render(request,'user.html')