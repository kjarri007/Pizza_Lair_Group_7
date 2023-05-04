from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product import models
from product.models import Pizza


# Create your views here.

def pizza_index(request):
    all_pizzas = Pizza.objects.all().order_by('price')
    if 'sort_by' not in request.GET:
        all_categories = models.Category.objects.all()
        return render(request, 'product/pizza_index.html',
                      context={"all_pizzas": all_pizzas, "all_categories": all_categories})

    order = request.GET['order']

    # If the user searches pizzas by name
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        filtered_pizzas = all_pizzas.filter(name__icontains=search_filter).order_by(order)
        return JsonResponse({"data": filtered_pizzas})

    # If the user presses a category button to filter pizzas by category
    elif 'category_filter' in request.GET:
        category = request.GET['category_filter']
        filtered_pizzas = all_pizzas.filter(categories__exact=category).order_by(order)
        return JsonResponse({"data": filtered_pizzas})


def offer_index(request):
    all_offers = models.Offer.objects.all()
    return render(request, "product/offer_index.html", context={"all_offers": all_offers})


def pizza_detail(request, pizza_id):
    selected_pizza = get_object_or_404(models.Pizza, pk=pizza_id)
    return render(request, "product/pizza_detail.html", context={"selected_pizza": selected_pizza})


def offer_detail(request, offer_id):
    selected_offer = get_object_or_404(models.Offer, pk=offer_id)
    return render(request, "product/offer_detail.html", context={"selected_offer": selected_offer})
