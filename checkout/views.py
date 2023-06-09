from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from user.models import Cart, Profile
from .forms.contact import ContactInfoForm
from .forms.payment_detail import PaymentDetailsForm
from checkout.models import ContactInfo, PaymentDetails


# Create your views here.
@login_required
def contact_info(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    if user_cart.is_empty():
        return redirect("main_page")
    user_contact_info = ContactInfo.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ContactInfoForm(instance=user_contact_info, data=request.POST)
        if form.is_valid():
            user_contact_info = form.save(commit=False)
            user_contact_info.user = request.user
            user_contact_info.save()
            if "back_to_cart" in request.POST:
                return redirect("user_cart")
            elif "payment_detail" in request.POST:
                return redirect("payment_detail")
            elif "pickup" in request.POST:
                user_payment_info = PaymentDetails.objects.filter(user=request.user).first()
                if user_payment_info:
                    return redirect("review_order")
    else:
        profile_contact_info = Profile.objects.filter(user=request.user).first()
        if not user_contact_info:
            form = ContactInfoForm(instance=profile_contact_info)
        else:
            form = ContactInfoForm(instance=user_contact_info)
    context = {"form": form}
    return render(request, "checkout/contact_info.html", context=context)


@login_required
def payment_info(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    if user_cart.is_empty():
        return redirect("main_page")
    user_payment_info = PaymentDetails.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = PaymentDetailsForm(instance=user_payment_info, data=request.POST)
        if form.is_valid():
            user_payment_info = form.save(commit=False)
            user_payment_info.user = request.user
            user_payment_info.save()
        if "contact_info" in request.POST:
            return redirect("contact_info")
        elif "review_order" in request.POST:
            return redirect("review_order")
    else:
        form = PaymentDetailsForm(instance=user_payment_info)
    context = {"form": form}
    return render(request, "checkout/payment_info.html", context=context)


@login_required
def review_step(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    if user_cart.is_empty():
        return redirect("main_page")
    user_payment_info = PaymentDetails.objects.filter(user=request.user).first()  # needs to be erased when POST
    user_contact_info = ContactInfo.objects.filter(user=request.user).first()  # needs to be erased when POST
    return render(request, "checkout/review_order.html",
                  context={"cart": user_cart, "contact_info": user_contact_info, "payment_info": user_payment_info})


@login_required
def confirmation(request):
    user_cart = Cart.objects.filter(user=request.user).first()
    user_contact_info = ContactInfo.objects.filter(user=request.user).first()  # needs to be erased when POST
    if user_contact_info:
        user_contact_info.delete()
        user_cart.clear_cart()
        user_cart.save()
        user_payment_info = PaymentDetails.objects.filter(user=request.user).first()  # needs to be erased when POST
        if user_payment_info:
            user_payment_info.delete()
    return render(request, "checkout/thank_you.html")
