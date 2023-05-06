from django.http import JsonResponse  # Throw away after testing
from django.shortcuts import render
from .forms.contact import ContactInfoForm
from .forms.payment import PaymentForm


# Create your views here.
def contact_info(request):
    if request.method == "POST":
        pass
    return render(request, "checkout/contact_info.html", context={"form": ContactInfoForm()})


def payment_info(request):
    if request.method == "POST":
        pass
    return render(request, "checkout/payment_info.html", context={"form": PaymentForm()})


def review_step(request):
    if request.method == "POST":
        pass
    return render(request, "checkout/review_order.html", context={})


def confirmation(request):
    return render(request, "checkout/thank_you.html")
