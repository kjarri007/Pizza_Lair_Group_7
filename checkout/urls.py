from django.urls import path
from . import views

urlpatterns = [
    path("contact-info/", views.contact_info, name="contact_info"),
    path("payment-detail/", views.payment_info, name="payment_info"),
    path("review/", views.review_step, name="review_order"),
    path("confirmation/", views.confirmation, name="order_confirmation")
]
