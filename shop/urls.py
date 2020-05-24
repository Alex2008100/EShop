from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('product/<int:pk>', views.product, name='product'),
]
