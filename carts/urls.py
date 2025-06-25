from django.urls import path
from carts import views

urlpatterns = [
    # Define cart-related URL patterns here
    path("", views.cart, name="cart"),
    path("add_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
]
