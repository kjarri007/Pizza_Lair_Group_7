import uuid

from django.contrib.auth.models import User
from django.db import models
from product.models import Product


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def clear_cart(self):
        cart_items = self.cart_items.all()
        cart_items.delete()

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cart_items = self.cart_items.all()
        total = sum([item.price for item in cart_items])
        return total

    @property
    def num_of_items(self):
        cart_items = self.cart_items.all()
        quantity = sum([item.quantity for item in cart_items])
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product

    @property
    def price(self):
        price_total = self.product.price * self.quantity
        return price_total
