from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Category(models.Model):
    CARTEGORY = [
        ('Computing', 'computing'),
        ('Electronics', 'electronics'),
        ('Sporting','sporting' ),
        ('Fashion', 'fashion'),
        ('Automobile', 'automobile'),
        ('Toys&Games', 'toys&games'),
        ('Phones', 'phones'),
        ('Musical', 'Musical')
    ]
    category_name = models.CharField(max_length=255, choices=CARTEGORY)
    
    
    def __str__(self):
        return self.category_name
    
    
    
class Product(models.Model):

    product_id = models.BigAutoField(primary_key=True, editable=False)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField()
    product_description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=8)
    old_price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name
    
    def get_total_saved(self):
        return self.old_price - self.unit_price
    
    
    
class Customer(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    email = models.EmailField()
    orders = models.PositiveIntegerField(blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'   
    

    