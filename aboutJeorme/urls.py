from django.urls import path
from . import views

urlpatterns = [
    path("aboutJeorme/", views.AboutJerome),
]

