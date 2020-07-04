from django import forms
from .models import Product, Purchase, ItemsBack


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(required=True)


"""
    def clean_quantity(self):
        product=Product.object.get(name=item.name)
        if self.data['quantity'] > Product.amount
            raise forms.ValidationError('Stock does not have enough items')
        return self.data['quantity']
"""


class ItemUpdatingForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'amount')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'amount')


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('amount', 'product')


class ItemsBackForm(forms.ModelForm):
    class Meta:
        model = ItemsBack
        fields = ('item',)
