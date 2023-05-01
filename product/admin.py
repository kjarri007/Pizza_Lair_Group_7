from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Offer)
admin.site.register(Topping)
admin.site.register(Category)
admin.site.register(PizzaImg)
admin.site.register(OfferImg)
