from django.contrib.auth.models import User
from django.db import models
# from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from product.models import Product


# Create your models here.
class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=255)
    card_number = models.IntegerField()
    expiration_date = models.DateField()
    cvc_number = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    total_price = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()

    def __str__(self):
        return str(self.product.name)
