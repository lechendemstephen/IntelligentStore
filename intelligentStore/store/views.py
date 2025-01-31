from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from comment.models import Comments  # import the comment model
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
    comment = Comments.objects.filter(product=single_product) # get all comments for the product


    context = {
        "single_product": single_product, 
        'comments': comment 
    }


    return render(request, 'pages/public/single_product.html', context )

# post comment 
def post_comment(request, product_name): 
    single_product = get_object_or_404(Product, slug=product_name) 
    comment = Comments.objects.filter(product=single_product) # get all comments for the product
    name = request.user.username # get the username of the user 
    if request.method == "POST": 
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        Comments.objects.create(name=name, comment=comment, product=single_product)
        return redirect('single_product', product_name=product_name)
    context = {
        "single_product": single_product, 
        'comments': comment 
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