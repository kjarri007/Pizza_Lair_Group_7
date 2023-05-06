from django.contrib.auth.models import User
from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from product.models import Product


# Create your models here.
class ContactInfo(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)


class Payment(models.Model):
    card_holder = models.CharField(max_length=255)
    card_number = CardNumberField('card number')
    expiration_date = CardExpiryField('expiration date')
    cvc_number = SecurityCodeField('security code')


class OrderItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)


class Order(models.Model):
    contact_id = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True)

    def calculate_total_price(self):
        total_price = 0
        for item in self.orderitem_set.all():
            total_price += item.product_id.price
        return total_price
