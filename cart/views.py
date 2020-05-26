from django.shortcuts import render
from .models import Product
# Create your views here.

def cart(request):
    products = Product.object.all()#filter(in_cart=True)
    render(request, 'cart/shopping-cart.html', {'product_list':products})
