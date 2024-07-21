# from django.urls import path
# from . import views

# urlpatterns = [
#     path('booking/', views.booking_calendar, name='booking_calendar'),
#     path('booking/<str:base_date>/', views.booking_calendar, name='booking_calendar'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking_calendar, name='booking_calendar'),
    path('booking/<int:year>/<int:month>/<int:day>/', views.booking_calendar, name='booking_calendar_with_date'),
]
