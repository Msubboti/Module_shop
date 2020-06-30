from django.shortcuts import render
from django.views.generic import ListView


from .models import Product

# Create your views here.


def index(request):
    return render(request, 'product/base.html',)


class ProductList(ListView):
    model = Product
