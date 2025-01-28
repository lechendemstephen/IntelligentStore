from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Cart
from store.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login/')
def add_to_cart(request, product_id): 
    product = get_object_or_404(Product, id=product_id)

    # creating the add to cart functionality 
    cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
    if not created: 
        cart_item.quantity +=1 
        cart_item.save() 
    
    return redirect("cart")

# show all cart items 
@login_required(login_url='login')
def cart_item(request): 
    # getting all cart items 
    items = Cart.objects.all() 

    context = {
        'cart_items': items 
    }

    return render(request, 'pages/public/cart.html', context)