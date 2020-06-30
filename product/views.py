from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView


from .models import Product
from .forms import ItemUpdatingForm

# Create your views here.


def index(request):
    return render(request, 'product/base.html',)


class ProductList(ListView):
    model = Product


class ItemUpdate(UpdateView):
    model = Product
    form_class = ItemUpdatingForm
    template_name = 'product/ItemUpdate.html'
    success_url = reverse_lazy('product:store_offers')
