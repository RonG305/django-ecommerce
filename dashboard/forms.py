from django import forms
from shop.models import Product

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_image',
            'product_name',
            'product_description',
            'quantity',
            'unit_price',
            'old_price',
            'category'
        ]
        
        labels = {
             'product_image': 'product image',
            'product_name': 'product name',
            'product_description': 'description',
            'quantity': 'quantity',
            'unit_price': 'unit price',
            'old_price': 'old price',
            'category': 'category' 
        }
        
        
    
    