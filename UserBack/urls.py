from django.urls import path
from UserBack import views

urlpatterns = [
    path("feedback/", views.UserBack),
]
