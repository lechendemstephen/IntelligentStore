from django.db import models
from store.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name
    

