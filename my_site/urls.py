from django.urls import path
from . import views

urlpatterns = [
    path("", views.front_page, name="main_page")
]
