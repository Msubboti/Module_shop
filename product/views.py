from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from datetime import timedelta
from django.utils import timezone


from .models import Product, Purchase, ItemsBack
from users.models import User
from .forms import ItemUpdatingForm, ProductForm, PurchaseForm, ItemsBackForm

# Create your views here.


def index(request):
    return render(request, 'product/base.html',)


class ProductList(ListView):
    model = Product
    ordering = ['name']


class ItemUpdate(UpdateView):
    model = Product
    form_class = ItemUpdatingForm
    template_name = 'product/ItemUpdate.html'
    success_url = reverse_lazy('product:store_offers')


class CreateNewProduct(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:store_offers')
    template_name = 'product/CreateProduct.html'

    def form_valid(self, form):
        """If image is not set, the default image will be set automatically"""
        data = form.data['image']
        if data == "":
            self.object = form.save(commit=False)
            self.object.image = 'media/product/images/default_img.png'
            self.object.save()
        return super().form_valid(form)


class CreatingPurchases(CreateView):
    model = Purchase
    form_class = PurchaseForm
    success_url = reverse_lazy('product:store_offers')

    def get_initial(self):
        initial = {'product': self.kwargs.get('pk')}
        return initial

    def form_valid(self, form):
        """If image is not set, the default image will be set automatically"""
        user = User.objects.get(username=self.request.user)
        product = Product.objects.get(pk=int(form.data['product']))
        if user.wallet < product.price and product.amount > int(form.data['amount']):
            messages.add_message(self.request, messages.WARNING, 'It is possible that you don\'t have enough money for trading transactions in the account.')
        elif user.wallet > product.price and product.amount < int(form.data['amount']):
            messages.add_message(self.request, messages.WARNING, 'We have just {}, if you need more,please contact to administrator'.format(product.amount))
        else:
            user.wallet -= product.price * int(form.data['amount'])
            user.save()
            product.amount -= int(form.data['amount'])
            product.save()
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.status = self.object.NEW
            self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Data is incorrect')
        return super(CreatingPurchases, self).form_invalid(form)


class PurchaseList(ListView):
    model = Purchase
    ordering = ['-created_at']

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model.objects.filter(user=self.request.user.pk)
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset


class ReturnPurchase(CreateView):
    model = ItemsBack
    form_class = ItemsBackForm
    success_url = reverse_lazy('product:my_purchases')

    def get_initial(self):
        initial = {'purchase': self.kwargs.get('pk')}
        return initial

    def form_valid(self, form):
        """If image is not set, the default image will be set automatically"""
        purchase = Purchase.objects.get(pk=int(form.data['item_back']))
        time_purchase = purchase.created_at
        delete_time = time_purchase + timedelta(minutes=3)
        if timezone.now() > delete_time:
            messages.add_message(self.request, messages.WARNING,
                                 'Sorry, the purchase might be returned during 3 minutes after time of order')
        else:
            purchase.status = purchase.REVIEW
            purchase.save()
            self.object = form.save(commit=False)
            self.object.item = purchase
            self.object.save()
        return super().form_valid(form)


class ReturningList(ListView):
    model = ItemsBack
    ordering = ['-created_at']


class QueryApproval(DeleteView):
    model = ItemsBack
    success_url = reverse_lazy('product:returning_list')

    def get_object(self, queryset=None):
        return_item = ItemsBack.objects.get(pk=self.kwargs['pk'])
        customer = return_item.item.user
        purchase = return_item.item
        product = purchase.product
        if self.request.POST.get('approval') != None:
            customer.wallet += purchase.product.price * purchase.amount
            customer.save()
            product.amount += purchase.amount
            product.save()
            purchase.status = purchase.APPROVED
        elif self.request.POST.get('rejected') != None:
            purchase.status = purchase.REJECTED
        purchase.save()
        return super().get_object()
