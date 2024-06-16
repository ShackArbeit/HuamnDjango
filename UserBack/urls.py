from django.urls import path
from UserBack import views

urlpatterns = [
    path("feedback/", views.UserBack),
    path("feedback/list",views.listing),
    path("feedback/post",views.posting),
    path("feedback/delpost/<int:pid>/<str:del_pass>/",views.delpost)
]