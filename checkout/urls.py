from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("contact/", views.contact, name="contact_info"),
    path("payment/", views.payment, name="payment_info"),
    path("review/", views.review, name="review_order"),
    path("process/", views.process, name="thank_you")
]
