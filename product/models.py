from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)


class Topping(models.Model):
    name = models.CharField(max_length=50)


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    toppings = models.ManyToManyField(Topping)
    categories = models.ManyToManyField(Category)
    price = models.IntegerField()


class Offers(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pizzas = models.ManyToManyField(Pizza)
    price = models.IntegerField()


class PizzaImg(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)


class OfferImg(models.Model):
    image = models.CharField(max_length=9999)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
