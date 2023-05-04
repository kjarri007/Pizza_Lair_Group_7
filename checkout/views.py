from django.shortcuts import render


# Create your views here.
def cart(request):
    return render(request, 'checkout/cart.html')


def contact(request):
    return render(request, 'checkout/contact_info.html')


def payment(request):
    return render(request, 'checkout/payment_info.html')


def review(request):
    return render(request, 'checkout/review_order.html')


def process(request):
    return render(request, 'checkout/thank_you.html')
