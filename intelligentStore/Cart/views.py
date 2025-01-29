from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from store.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_cart(request, product_id): 
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    # creating the add to cart functionality 
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    if not created: 
        cart_item.quantity +=1 
        cart_item.save() 
    
    return redirect("cart")

# show all cart items 
@login_required
def cart_item(request):
    try: 
    # cart 
        cart = Cart.objects.get(user=request.user) 
        # getting all cart items 
        items = CartItem.objects.filter(cart=cart)
        print(items)
    except Cart.DoesNotExist: 
        items = [] 

    context = {
        'items': items 
    }

    return render(request, 'pages/public/cart.html', context)