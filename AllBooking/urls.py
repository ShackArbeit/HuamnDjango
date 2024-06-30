from django.urls import path
from . import views

urlpatterns = [
    path("booking/", views.booking_list,{'week_offset':0},name='booking_list'),
    path('booking/<int:week_offset>/', views.booking_list, name='booking_list'),
]
