from django.shortcuts import render
from .models import Client, ProductInCart
from shop.models import Product
from .serializers import ClientSerializer, ProductSerializer, ProductInCartSerializer
from rest_framework import generics

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductInCartListCreate(generics.ListCreateAPIView):
    queryset = ProductInCart.objects.all()
    serializer_class = ProductInCartSerializer

def test(request):
    return render(request, 'test.html', {})
