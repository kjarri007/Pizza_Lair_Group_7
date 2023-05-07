from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


def profile(request):
    # user_profile = get_object_or_404(Profile, pk=request.user)
    user_profile = Profile.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = ProfileForm(instance=user_profile, data=request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect("profile")
    return render(request, "user/profile.html", context={"form": ProfileForm(instance=user_profile)})


def add_to_cart(request, product_id):
    user_cart = request.user.cart
    selected_product = get_object_or_404(Product, pk=product_id)
    for item in list(user_cart.cartitem_set.all()):
        if item.product.id == product_id:
            item.quantity += 1
            redirect("user_cart")
    cart_item = CartItem(product=selected_product, cart=user_cart)
    cart_item.save()
    return redirect("user_cart")


def cart(request):
    user_cart = request.user.cart
    cart_items = user_cart.cartitem_set.all()
    # cart_items = models.CartItem.objects.filter(cart=user_cart)
    return render(request, "user/cart.html", context={"user_cart": user_cart, "cart_items": cart_items})
