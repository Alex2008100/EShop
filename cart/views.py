from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Product
from cart.models import Cart, CartItem
# Create your views here.

def cart(request):
    products = Product.objects.filter(in_cart = True)
    return render(request, 'shopping-cart.html', {'products':products})


'''
def add_to_cart(request,pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.get_or_create(user=request.user)
    cart_item = CartItem.objects.get_or_create(product=product, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
'''

def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart = Cart(request)
    cart.add(product, product.price_sell)
'''
def remove_from_cart(request, pk):
    product = Product.objects.get(id=pk)
    cart = Cart(request)
    cart.remove(product)
'''

def get_cart(request):
    return render(request, 'shopping-cart.html', {'cart': Cart(request)})
