from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.


# function for the homepage 
def index(request): 
    all_products = Product.objects.all()


    context = {
        'products': all_products
    }


    return render(request, 'pages/public/index.html', context)


# shop preview 
def shop(request): 
    all_products = Product.objects.all()


    context = {
        'products': all_products
    }
    return render(request, 'pages/public/shop.html', context)




# orders preview
def orders(request): 

    return render(request, 'pages/public/orders.html')


#single product_display 
def single_product(request, product_name): 
    single_product = get_object_or_404(Product, slug=product_name) 


    context = {
        "single_product": single_product
    }


    return render(request, 'pages/public/single_product.html', context )



#checkout
def checkout(request): 

    return render(request, 'pages/public/checkout.html')








# account dashboard 

def account_settings(request): 

    return render(request, 'account/account_email.html')

#account overview 
@login_required(login_url='account_login')
def account_overview(request): 

    return render(request, 'pages/public/account_overview.html')