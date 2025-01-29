from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.
class CartAdmin(admin.ModelAdmin): 
    list_display = ('user', 'date')

class CartItemAdmin(admin.ModelAdmin): 
    list_display = ('cart', 'product', 'quantity')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

