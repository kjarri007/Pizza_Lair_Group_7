from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product import models
from product.models import Pizza


# Create your views here.

def pizza_index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [{
            'id': pizza.id,
            'name': pizza.name,
            'description': pizza.description,
            'firstImage': pizza.pizzaimg_set.first().image
        } for pizza in Pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas})

    context = {'pizzas': Pizza.objects.all().order_by('name')}
    # TODO: Create a html file "pizza_index.html"
    all_pizzas = models.Pizza.objects.all()
    return render(request, 'product/pizza_index.html', context={"all_pizzas": all_pizzas})


def offer_index(request):
    all_offers = models.Offer.objects.all()
    return render(request, "product/offer_index.html", context={"all_offers": all_offers})


def pizza_detail(request, pizza_id):
    selected_pizza = get_object_or_404(models.Pizza, pk=pizza_id)
    return render(request, "product/pizza_detail.html", context={"selected_pizza": selected_pizza})


def offer_detail(request, offer_id):
    selected_offer = get_object_or_404(models.Offer, pk=offer_id)
    return render(request, "product/offer_detail.html", context={"selected_offer": selected_offer})
