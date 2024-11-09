from django import forms

from django.shortcuts import render

tasks = [ "shop", "work", "pray", "eat", "sleep" ]	

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=8)

# Create your views here.
def index(request):
    # now we will pass those tasks in an array as an argument and catch them in the html file
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        # validating the data in the server side
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })