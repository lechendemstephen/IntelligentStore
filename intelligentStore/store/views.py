from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


# function for the homepage 
def index(request): 

    return render(request, 'pages/public/index.html')


# shop preview 
def shop(request): 

    return render(request, 'pages/public/shop.html')


# orders preview
def orders(request): 

    return render(request, 'pages/public/orders.html')


# cart preview
def cart(request): 

    return render(request, 'pages/public/cart.html')

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