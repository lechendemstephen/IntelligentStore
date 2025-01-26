from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='home'), 
    path('shop/', views.shop, name='shop'), 
    path('order/', views.orders, name='order'),
    path('cart/', views.cart, name='cart'),
    path("checkout/", views.checkout, name="checkout"),
    path("shop/<product_name>/", views.single_product, name="single_product"),



    # user settings 
    path('accounts/email/', views.account_settings, name='account_email'),
    path('account_overview/', views.account_overview, name='account_overview'),

]
