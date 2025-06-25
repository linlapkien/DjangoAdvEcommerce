from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from store.models import Product
from django.http import HttpResponse

# Create your views here.

def cart(request, total=0, quantity=0, cart_items=None):
    """
    Render the cart page.
    """
    try:
        cart = Cart.objects.get(card_id=_cart_id(request))  # Get the cart using the session ID
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)  # Get active cart items
        for item in cart_items:
            total += (item.product.price * item.quantity)  # Calculate total price
            quantity += item.quantity  # Calculate total quantity
    except ObjectDoesNotExist:
        # If the cart does not exist, initialize total and quantity
        pass # Just pass if cart does not exist

    context = {
        'total': total,  # Total price of items in the cart
        'quantity': quantity,  # Total quantity of items in the cart
        'cart_items': cart_items,  # List of items in the cart
    }

    return render(request, 'store/cart.html', context)

def _cart_id(request):
    """
    Generate a unique cart ID for the session.
    """
    cart_id = request.session.session_key  # Get the session key as cart ID
    if not cart_id:
        cart_id = request.session.create()  # Create a new session if it doesn't exist

    return cart_id

def add_to_cart(request, product_id):
    """
    Add a product to the cart.
    """
    # Logic to add the product to the cart
    product = Product.objects.get(id=product_id) # Get the product by ID

    try:
        cart = Cart.objects.get(card_id=_cart_id(request))  # Get the cart using the session ID
    except Cart.DoesNotExist:
        cart = Cart(card_id=_cart_id(request))  # Create a new cart if it doesn't exist
        cart.save()  # Save the new cart

    # Check if the product is already in the cart
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)  # Check if the product is already in the cart
        cart_item.quantity += 1  # Increment the quantity if it exists
        cart_item.save()  # Save the updated cart item
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,quantity = 1, cart=cart) # Create a new cart item if it doesn't exist
        cart_item.save()  # Save the new cart item

    return redirect('cart')  # Redirect to the cart page
