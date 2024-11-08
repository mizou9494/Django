from django.shortcuts import render
from django.http import HttpResponse

tasks = [ "shop", "work", "pray", "eat", "sleep" ]	
# Create your views here.
def index(request):
    # now we will pass those tasks in an array as an argument and catch them in the html file
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")