from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms.profile import ProfileForm
from user.models import Profile, CartItem, Cart
from product.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


# Create your views here
def register(request):
    # Could be either a POST or GET request!

    # If it's a POST request, gather the data from the HTTP body in a form variable,
    # check if its valid, if it is then store it and redirect the user to the login screen.
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    # If it's a GET request, then send a render request to the 'register.html' file and send
    # Django built-in form as context.
    return render(request, "user/register.html", context={"form": UserCreationForm()})


@login_required
def profile(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect("user_profile")
    else:
        form = ProfileForm(instance=user_profile)
    context = {"form": form}
    return render(request, "user/profile.html", context=context)

@login_required
def add_to_cart(request, product_id):
    selected_product = get_object_or_404(Product, pk=product_id)
    user_cart = request.user.cart
    user_cart.add_to_cart(selected_product)
    return redirect("user_cart")


@login_required
def cart(request):
    def create_cart_items(queryset):
        all_items = [{
            'id': item.id,
            'name': item.product.name,
            'price': item.product.price,
            'total_price': item.price,
            'quantity': item.quantity,
            'firstImage': item.product.productimg_set.first().image
        } for item in queryset]
        return all_items

    user_cart = request.user.cart

    if request.method == "POST":
        command = request.GET["command"]
        if command == "clear":
            user_cart.clear_cart()
            user_cart.save()
            return JsonResponse({"total_price": user_cart.total_price, "num_of_items": user_cart.num_of_items})
        elif command == "remove":
            user_cart.remove_item(request.GET["item"])
            user_cart.save()
            if user_cart.is_empty():
                remove_button = True
            else:
                remove_button = False
            return JsonResponse({"total_price": user_cart.total_price,
                                 "num_of_items": user_cart.num_of_items, "remove_checkout_button": remove_button})
        elif command == "update-quantity":
            item_id = request.GET["item"]
            new_quantity = request.GET["quantity"]
            user_cart.update_quantity(item_id, new_quantity)
            selected_item = CartItem.objects.get(pk=item_id)
            new_item_price = selected_item.price
            new_cart_price = user_cart.total_price
            num_of_items = user_cart.num_of_items
            return JsonResponse({"cart_price": new_cart_price, "item_price": new_item_price, "num_of_items": num_of_items})
    user_cart = Cart.objects.get(user=request.user)
    cart_items = user_cart.cartitem_set.all()
    if user_cart.is_empty():
        is_empty = True
    else:
        is_empty = False
    context = {
        "user_cart": user_cart,
        "cart_items": cart_items,
        "is_empty": is_empty
    }
    return render(request, "user/cart.html", context=context)
