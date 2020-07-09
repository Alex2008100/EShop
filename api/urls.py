from django.urls import path
from . import views

urlpatterns = [
    #Main APIs
    path('users/', views.ClientListCreate.as_view()),
    path('product/', views.ProductListCreate.as_view()),
    path('cart/', views.ProductInCartListCreate.as_view()),
    path('test', views.test),
]
