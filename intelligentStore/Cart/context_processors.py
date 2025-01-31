from .models import CartItem 
from django.contrib.auth.decorators import login_required

# cart item count 
@login_required
def cart_item_count(request): 
    cart = CartItem.objects.filter(cart__user=request.user)
    count = 0 
    for item in cart: 
        count += item.quantity
    return {'cart_item_count': count}

# list of cart items 
@login_required 
def cart_items(request): 
    cart = CartItem.objects.filter(cart__user=request.user)
    return {'cart_items': cart}