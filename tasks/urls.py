from django.urls import path

from . import views

# the app name is because we have that one route named index
app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
]