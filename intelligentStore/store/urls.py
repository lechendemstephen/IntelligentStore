from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='home'), 
    path('shop/', views.shop, name='shop'), 
    path('order/', views.orders, name='order'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),

    # authentication 
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    



]
