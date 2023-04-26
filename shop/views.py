from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from shop.models import Product, Category
from .forms import ProductSearchForm
from dashboard.forms import ProductCreationForm

# Create your views here.

def shop(request):
    return render(request, 'shop/shop.html')

def product(request):
    category = request.GET.get('category')
    if category == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__category_name=category)    
        
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/product.html', context)



def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    decimal_discount = (product.old_price - product.unit_price) / product.old_price * 100
    discount = round(decimal_discount, 2)
    
    context = {
        'product': product,
        'discount': discount
    }
    return render(request, 'shop/product_details.html', context)


def shopping_cart(request):
    return render(request, 'shop/shopping_cart.html')

def checkout(request):
    return render(request, 'shop/checkout.html')