from django.urls import path
from . import views

urlpatterns = [
    path("what/", views.Hover_Layout),
    path("what/<str:sub_router>",views.Human_Books)
]

