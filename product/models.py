from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=1000)


class Pizza(Product):
    toppings = models.ManyToManyField(Topping)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Offer(Product):
    pizzas = models.ManyToManyField(Pizza)

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    image = models.CharField(max_length=9999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
