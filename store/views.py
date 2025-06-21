from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    """
    Render the store page with products.
    If a category slug is provided, filter products by that category.
    """
    categories = None
    products = None

    if category_slug is not None:
        # Filter products by category slug
        # get_object_or_404 is used to retrieve the category object or return a 404 error if not found
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        # Total number of products in the selected category
        product_count = products.count()

    else:
        # If no category slug, get all available products
        products = Product.objects.all().filter(is_available=True)
        # Total number of products available
        product_count = products.count()


    context = {
        'products': products,
        'product_count': product_count,
    }

    return render(request, 'store/store.html', context)