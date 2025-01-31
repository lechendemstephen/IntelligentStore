from django.db import models
from store.models import Product
# Create your models here.
class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_on']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    