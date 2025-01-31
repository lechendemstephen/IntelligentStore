from django.db import models
from store.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class CartItem(models.Model): 
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
    
    @property 
    def total(self): 
        return self.product.price * self.quantity 
    

