from django.shortcuts import render
from django.http import HttpResponse

tasks = [ "shop", "work", "pray", "eat"]
# Create your views here.
def index(request):
    # now = datetime.datetime.now()
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")