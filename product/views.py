from django.shortcuts import render, get_object_or_404

from product import models


# Create your views here.

def pizza_index(request):
    all_pizzas = models.Pizza.objects.all()
    return render(request, "#", context={"all_pizzas": all_pizzas})


def offer_index(request):
    all_offers = models.Offer.objects.all()
    return render(request, "#", context={"all_offers": all_offers})


def pizza_detail(request, pizza_id):
    selected_pizza = get_object_or_404(models.Pizza, pk=pizza_id)
    return render(request, "#", context={"selected_pizza": selected_pizza})


def offer_detail(request, offer_id):
    selected_offer = get_object_or_404(models.Offer, pk=offer_id)
    return render(request, "#", context={"selected_offer": selected_offer})
