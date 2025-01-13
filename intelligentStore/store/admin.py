from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'category', 'price', 'description', 'slug', 'stock')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)