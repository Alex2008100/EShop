from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base/base.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def cart(request):
    return render(request, 'shopping-cart.html', {})

def product(request):
    return render(request, 'product.html', {})


