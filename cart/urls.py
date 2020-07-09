from django.urls import path
from . import views

urlpatterns = [
    #Main cart urls
    path('', views.cart, name="cart"),
    path('add/<int:pk>', views.add_to_cart, name="add_to_cart"),
    path('show_cart', views.get_cart, name="get_cart"),
]
