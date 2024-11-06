from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html") 

def hamza(request):
    return HttpResponse("Hello, Hamza!")

def ilham(request):
    return HttpResponse("Hello, Ilham!")

def radia(request):
    return HttpResponse("Hello, Radia!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    }) 
    