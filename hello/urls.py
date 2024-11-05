from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/hamza", views.hamza, name="hamza")
]