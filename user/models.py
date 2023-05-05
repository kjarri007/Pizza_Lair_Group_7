import uuid

from django.contrib.auth.models import User
from django.db import models
from product.models import Pizza, Offer


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)


class Product(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)
    price = Pizza.price  # vantar fyrir offer lika


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

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
        new_price = self.product.price * self.quantity
        return new_price
