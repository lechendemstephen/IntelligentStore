from django.shortcuts import render

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


# account preview
def account(request): 

    return render(request, 'pages/account/account_preview.html')

# cart preview
def cart(request): 

    return render(request, 'pages/public/cart.html')



# authentication 



def signup(request): 

    return render(request, 'pages/authentication/signup.html')



def login(request): 

    return render(request, 'pages/authentication/login.html')


