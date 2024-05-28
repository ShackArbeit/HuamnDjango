from django.urls import path
from . import views

urlpatterns = [
    path("what/", views.Hover_Layout),
    path("what/<str:sub_router>",views.Human_Books,name='human_books'),
    path("what/<str:sub_router2>",views.Human_Types,name='human_types')
]

