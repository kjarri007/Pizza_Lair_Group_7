from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product import models
from product.models import Pizza


# Create your views here.

def pizza_index(request):
    # If the user searches pizzas by name
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [{
            'id': pizza.id,
            'name': pizza.name,
            'description': pizza.description,
            'firstImage': pizza.pizzaimg_set.first().image
        } for pizza in Pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas})

    # If the user presses a category button to filter pizzas by category
    elif 'category_filter' in request.GET:
        category_id = request.GET['category_filter']
        if category_id == '0':
            pizzas = [{
                'id': pizza.id,
                'name': pizza.name,
                'description': pizza.description,
                'firstImage': pizza.pizzaimg_set.first().image
            } for pizza in Pizza.objects.all().order_by('price')]
        else:
            category = get_object_or_404(models.Category, pk=category_id)
            pizzas = [{
                'id': pizza.id,
                'name': pizza.name,
                'description': pizza.description,
                'firstImage': pizza.pizzaimg_set.first().image
            } for pizza in Pizza.objects.filter(categories=category)]

        return JsonResponse({'data': pizzas})

    # If the user is visiting the link and not filtering in any way
    all_pizzas = models.Pizza.objects.all().order_by("price")
    all_categories = models.Category.objects.all()
    return render(request, 'product/pizza_index.html',
                  context={"all_pizzas": all_pizzas, "all_categories": all_categories})


def offer_index(request):
    all_offers = models.Offer.objects.all()
    return render(request, "product/offer_index.html", context={"all_offers": all_offers})


def pizza_detail(request, pizza_id):
    selected_pizza = get_object_or_404(models.Pizza, pk=pizza_id)
    return render(request, "product/pizza_detail.html", context={"selected_pizza": selected_pizza})


def offer_detail(request, offer_id):
    selected_offer = get_object_or_404(models.Offer, pk=offer_id)
    return render(request, "product/offer_detail.html", context={"selected_offer": selected_offer})
