from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products/', views.product, name='product'),
    path('product_details/<str:product_id>/', views.product_details, name='product_details'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('checkout/', views.checkout, name='checkout')
    
]