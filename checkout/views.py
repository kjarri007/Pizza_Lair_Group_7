from django.http import JsonResponse  # Throw away after testing
from django.shortcuts import render
import json
from user.models import Product


# Create your views here.
def cart(request):
    products = Product.objects.all()
    context = {}
    return render(request, 'checkout/../templates/user/cart.html', context)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(product_id)
    return JsonResponse("it is working", safe=False)


def contact(request):
    return render(request, 'checkout/contact_info.html')


def payment(request):
    return render(request, 'checkout/payment_info.html')


def review(request):
    return render(request, 'checkout/review_order.html')


def process(request):
    return render(request, 'checkout/thank_you.html')
