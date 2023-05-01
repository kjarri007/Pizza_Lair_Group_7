from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    toppings = models.ManyToManyField(Topping)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Offer(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self):
        return self.name


class PizzaImg(models.Model):
    image = models.CharField(max_length=9999)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)


class OfferImg(models.Model):
    image = models.CharField(max_length=9999)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
