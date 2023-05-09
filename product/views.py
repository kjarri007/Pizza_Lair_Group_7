from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product import models
from product.models import Pizza


# Create your views here.
def front_page(request):
    return render(request, 'frontpage.html')


def pizza_index(request):
    # Helper function
    def create_pizza_list(queryset):
        pizzas = [{
            'id': pizza.id,
            'name': pizza.name,
            'description': pizza.description,
            'firstImage': pizza.productimg_set.first().image
        } for pizza in queryset]
        return pizzas

    all_pizzas = Pizza.objects.all().order_by('price')
    if 'order_by' not in request.GET:
        all_categories = models.Category.objects.all()
        return render(request, 'product/pizza_index.html',
                      context={"all_pizzas": all_pizzas, "all_categories": all_categories})

    order = request.GET['order_by']

    # If the user searches pizzas by name
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        filtered_pizzas = create_pizza_list(all_pizzas.filter(name__icontains=search_filter).order_by(order))
        return JsonResponse({"data": filtered_pizzas})

    # If the user presses a category button to filter pizzas by category
    elif 'category_filter' in request.GET:
        category = request.GET['category_filter'][-1]
        if category == '0':
            filtered_pizzas = create_pizza_list(Pizza.objects.all().order_by(order))
        else:
            filtered_pizzas = create_pizza_list(all_pizzas.filter(categories__exact=category).order_by(order))
        return JsonResponse({"data": filtered_pizzas})


def offer_index(request):
    all_offers = models.Offer.objects.all()
    return render(request, "product/offer_index.html", context={"all_offers": all_offers})


@login_required
def pizza_detail(request, pizza_id):
    selected_pizza = get_object_or_404(models.Pizza, pk=pizza_id)
    return render(request, "product/pizza_detail.html", context={"selected_pizza": selected_pizza})


@login_required
def offer_detail(request, offer_id):
    selected_offer = get_object_or_404(models.Offer, pk=offer_id)
    return render(request, "product/offer_detail.html", context={"selected_offer": selected_offer})
