from django.contrib import admin
from shop.models import Product, Category, Customer

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_image', 'product_name', 'product_description', 'quantity', 'category', 'unit_price']
    

admin.site.register(Category)
admin.site.register(Customer)
