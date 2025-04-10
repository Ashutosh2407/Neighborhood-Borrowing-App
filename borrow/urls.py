from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("users/", views.user_list, name = "user_list"),
    path("items/", views.item_list, name = "item_list")
]