from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="user_register"),
    path("login", LoginView.as_view(template_name="user/login.html"), name="user_login"),
    path("logout", LoginView.as_view(next_page="user_login"), name="user_logout")
]
