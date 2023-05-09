from django.http import JsonResponse  # Throw away after testing
from django.shortcuts import render, redirect

from user.models import Cart
from .forms.contact import ContactInfoForm
from .forms.payment_detail import PaymentDetailsForm
from checkout.models import ContactInfo, PaymentDetails


# Create your views here.
def contact_info(request):
    user_contact_info = ContactInfo.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ContactInfoForm(instance=user_contact_info, data=request.POST)
        if form.is_valid():
            user_contact_info = form.save(commit=False)
            user_contact_info.user = request.user
            user_contact_info.save()
            return redirect("payment_detail")
    return render(request, "checkout/contact_info.html", context={"form": ContactInfoForm(instance=user_contact_info)})


def payment_info(request):
    user_payment_info = PaymentDetails.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = PaymentDetailsForm(instance=user_payment_info, data=request.POST)
        if form.is_valid():
            user_payment_info = form.save(commit=False)
            user_payment_info.user = request.user
            user_payment_info.save()
            return redirect("review_order")
    return render(request, "checkout/payment_info.html",
                  context={"form": PaymentDetailsForm(instance=user_payment_info)})


def review_step(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    user_contact_info = ContactInfo.objects.filter(user=request.user).first()
    user_payment_info = PaymentDetails.objects.filter(user=request.user).first()
    if request.method == "POST":
        pass
    return render(request, "checkout/review_order.html",
                  context={"cart": user_cart, "contact_info": user_contact_info, "payment_info": user_payment_info})


def confirmation(request):
    return render(request, "checkout/thank_you.html")
