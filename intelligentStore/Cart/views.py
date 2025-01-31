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
    
     # cart 
    cart = Cart.objects.get(user=request.user)
    if cart: 
        
        # getting all cart items 
        items = CartItem.objects.filter(cart=cart)
        # Debug statement to log items
        total = 0 
        for item in items: 
            total += item.total
        # getting the total price of the items in the cart 
        tax = total * 0.08 
        # calculating the grand total 
        grand_total = total + tax
        
    else: 
        items = [] 
            # Debug statement to log empty cart
        

    context = {
        'items': items, 
        'total': total,
        'tax': tax,
        'grand_total': grand_total
    }

    # Debug statement to log context data
    print(f"Context data: {context}")

    return render(request, 'pages/public/cart.html', context)