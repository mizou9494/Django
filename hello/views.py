from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello there, world.") 

def hamza(request):
    return HttpResponse("Hello, Hamza!")

def ilham(request):
    return HttpResponse("Hello, Ilham!")

def radia(request):
    return HttpResponse("Hello, Radia!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")