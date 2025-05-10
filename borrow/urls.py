from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("users/", views.user_list, name = "user_list"),
    path("user/<int:pk>/", views.user_detail, name = "user-detail"),
    path("items/", views.item_list, name = "item_list"),
    path("item/<int:pk>/", views.item_detail, name = "item-detail"),
    path("item/<int:pk>/borrow/", views.item_borrow, name = "item_borrow"),
    path("item/<int:pk>/return/", views.item_return, name = "item_return"),
    path("groups/", views.group_list, name = "group_list"),
    path("groups/<int:pk>/", views.group_detail, name = "group-detail"),

]