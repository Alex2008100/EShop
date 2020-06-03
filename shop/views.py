from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from cart.models import Cart, CartItem

def index(request):
    return render(request, 'index.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product':product})
