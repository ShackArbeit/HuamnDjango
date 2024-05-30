from django.urls import path
from . import views

urlpatterns = [
    path("what/", views.Hover_Layout),
    path("what/1",views.Human_Books,name='human_books'),
    path("what/2",views.Human_Types,name='human_types'),
    path("what/3",views.Human_Roles,name='human_roles'),
    path("what/4",views.Human_Auths,name='human_auths'),
    path("what/5",views.Human_Energys,name='human_energy'),
    path("what/6",views.Human_Roads,name='human_road')
]

