from rest_framework import serializers
from .models import Client, ProductInCart
from shop.models import Product

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'message')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'brand', 'tag', 'in_cart', 'description', 'price_buy', 'price_sell', 'price_sell_no_discount', 'sku')

class ProductInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = ('sku', 'quantity')
