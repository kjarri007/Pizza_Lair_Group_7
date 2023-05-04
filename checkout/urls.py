from django.urls import path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    # path("contact/", ContactView.as_view(template_name="checkout/contact_info.html"), name="contact_info"),
    path("contact/", views.contact, name="contact_info"),
    # path("payment/", PaymentView.as_view(next_page="review_order"), name="payment_info"),
    path("payment/", views.payment, name="payment_info"),
    # path("review/", ReviewView.as_view(next_page="thank_you"), name="review_order"),
    path("review/", views.review, name="review_oder"),
    # path("process/", ThanksView.as_view(template_name="checkout/thank_you.html"), name="thank_you"),
    path("process/", views.process, name="thank_you")
]
