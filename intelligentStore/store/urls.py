from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='home'), 
    path('shop/', views.shop, name='shop'), 
    path('order/', views.orders, name='order'),
    path('cart/', views.cart, name='cart'),


    # user settings 
    path('accounts/email/', views.account_settings, name='account_email')

]
