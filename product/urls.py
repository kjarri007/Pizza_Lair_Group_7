from django.urls import path
from . import views

urlpatterns = [
    path("", views.front_page, name="main_page"),
    path("pizzas/", views.pizza_index, name="pizza_index"),
    path("offer/", views.offer_index, name="offer_index"),
    path("pizzas/<int:pizza_id>", views.pizza_detail, name="pizza_detail"),
    path("offer/<int:offer_id>", views.offer_detail, name="offer_detail"),
]
