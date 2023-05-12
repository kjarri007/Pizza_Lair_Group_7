from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)
    full_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    street_name = models.CharField(max_length=50)
    house_number = models.IntegerField()
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=30)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def is_empty(self):
        return self.num_of_items == 0

    def clear_cart(self):
        cart_items = self.cartitem_set.all()
        cart_items.delete()

        # if item.product.id == product_id:

    def add_to_cart(self, selected_product):
        for item in list(self.cartitem_set.all()):
            if item.product.id == selected_product.id:
                item.quantity += 1
                item.save(update_fields=["quantity"])
                return
        cart_item = CartItem(product=selected_product, cart=self)
        cart_item.save()

    def remove_item(self, item_id):
        item_to_remove = self.cartitem_set.get(pk=item_id)
        item_to_remove.delete()

    def update_quantity(self, item_id, new_quantity):
        item = self.cartitem_set.get(pk=item_id)
        item.quantity = new_quantity
        item.save()

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cart_items = self.cartitem_set.all()
        total = sum([item.price for item in cart_items])
        return total

    @property
    def num_of_items(self):
        cart_items = self.cartitem_set.all()
        quantity = sum([item.quantity for item in cart_items])
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product)

    @property
    def price(self):
        price_total = self.product.price * self.quantity
        return price_total
