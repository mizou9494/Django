from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hamza", views.hamza, name="hamza"),
    path("ilham", views.ilham, name="ilham"),
    path("radia", views.radia, name="radia"),
    # now instead of defining a route for each name we want to greet we will define a dynamic route that will take the "name" as a parameter which is a very useful feature 
    path("<str:name>", views.greet, name="greet"),
]