from rest_framework import serializers

from product.models import Product, Purchase
from users.models import User


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')


class PurchaseSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        price = obj.product.price
        amount = obj.amount
        return str(price*amount)

    class Meta:
        model = Purchase
        fields = ('user', 'product', 'total_price', 'created_at')


class UserHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'wallet')


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        return str(first_name + ' ' + last_name)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'wallet')
