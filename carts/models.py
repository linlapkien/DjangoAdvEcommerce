from django.db import models
from store.models import Product

# Create your models here.

class Cart(models.Model):
    """
    Model representing a shopping cart.
    """
    card_id = models.CharField(max_length=255, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.card_id


class CartItem(models.Model):
    """
    Model representing an item in the shopping cart.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def sub_total(self):
        """
        Calculate the subtotal for the cart item.
        """
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name