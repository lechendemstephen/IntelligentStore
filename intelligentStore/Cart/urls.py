from django.urls import path 
from . import views 
urlpatterns = [
    path('<product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_item, name='cart'),
   

]
