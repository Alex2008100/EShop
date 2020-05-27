from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    return render(request, 'index.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def cart(request):
    products = Product.objects.filter(in_cart = True)
    return render(request, 'shopping-cart.html', {'products':products})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product':product})
