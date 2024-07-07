from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking_calendar, name='booking_calendar'),
    path('booking/<str:base_date>/', views.booking_calendar, name='booking_calendar'),
]