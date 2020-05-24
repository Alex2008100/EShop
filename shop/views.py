from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def index(request):
    return render(request, 'base/base.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def cart(request):
    return render(request, 'shopping-cart.html', {})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product':product})


