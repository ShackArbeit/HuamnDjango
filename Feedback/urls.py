from django.urls import path
from . import views

urlpatterns = [
    path("feedback/",views.Feedback),
    path("feedback/list",views.Listing),
    path("feedback/post",views.Posting)
]
