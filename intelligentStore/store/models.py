from django.db import models

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Product(models.Model): 
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/products',)
    price = models.BigIntegerField()
    description = models.TextField(max_length=3000)
    slug = models.SlugField() 
    stock = models.IntegerField()

    def __str__(self):
        return self.name



