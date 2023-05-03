from django.shortcuts import render
from product import models


# Create your views here.
def front_page(request):
    return render(request, 'frontpage.html')
