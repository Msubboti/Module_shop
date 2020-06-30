from django import forms
from .models import Product


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

