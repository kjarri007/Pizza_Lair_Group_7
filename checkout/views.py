from django.http import JsonResponse  # Throw away after testing
from django.shortcuts import render, redirect
from .forms.contact import ContactInfoForm
from .forms.payment import PaymentForm
from checkout.models import ContactInfo, Payment, Order


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
    user_payment_info = Payment.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = PaymentForm(instance=user_payment_info, data=request.POST)
        if form.is_valid():
            user_payment_info = form.save(commit=False)
            user_payment_info.user = request.user
            user_payment_info.save()
            return redirect("review_order")
        else:
            # Access the first error message for the "card_number" field
            card_number_error = form.errors.get('card_number', None)
            if card_number_error:
                error_message = f"Invalid card number: {card_number_error}"
            else:
                error_message = "Please correct the errors below."
    else:
        error_message = None
    return render(request, "checkout/payment_info.html",
                  context={"form": PaymentForm(), "error_message": error_message})


def review_step(request):
    user_contact_info = ContactInfo.objects.filter(user=request.user).first()
    user_payment_info = Payment.objects.filter(user=request.user).first()
    if request.method == "POST":
        new_order = Order()
    return render(request, "checkout/review_order.html",
                  context={"contact_info": user_contact_info, "payment_info": user_payment_info})


def confirmation(request):
    return render(request, "checkout/thank_you.html")
