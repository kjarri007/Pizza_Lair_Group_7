from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("contact/", views.contact, name="contact_info"),
    path("payment/", views.payment, name="payment_info"),
    path("review/", views.review, name="review_oder"),
    path("process/", views.process, name="thank_you")
]
