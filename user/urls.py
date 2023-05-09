from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="user_register"),
    path("login", LoginView.as_view(template_name="user/login.html"), name="user_login"),
    path("logout", LogoutView.as_view(next_page="user_login"), name="user_logout"),
    path("profile", views.profile, name="user_profile"),
    path("cart/", views.cart, name="user_cart"),
    path("add-product/<int:product_id>", views.add_to_cart, name="add_to_cart")
]
