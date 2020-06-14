from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product
from .forms import UserRegisterForm, UserLoginForm

def index(request):
    return render(request, 'index.html', {})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products':products})

def product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product.html', {'product':product})

def register(request):

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            login(request, user)

        return redirect(index)
    else:
        return render(request, 'register.html', {'form':form})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = authenticate(request,
                username = form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password'))
            if user and user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'form':form})
        else:
            return render(request, 'login.html', {'form':form})

    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def product_output_test(request):
    products = Product.objects.all()
    return render(request, 'test0.html', {'products':products})
