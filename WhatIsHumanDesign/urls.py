from django.urls import path
from . import views

urlpatterns = [
    path("what/", views.Hover_Layout),
    path("what/1",views.Human_Books,name='human_books'),
    path("what/2",views.Human_Types,name='human_types')
]

