from django.contrib import admin
from .models import Comments # import the comment model
# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created_on', 'comment') # display the name, product, created_on, and comment
    list_filter = ('created_on',) # filter by created_on
    search_fields = ('name', 'comment') # search by name or comment



admin.site.register(Comments, CommentsAdmin) # register the comment model
