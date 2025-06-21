from category.models import Category

def menu_links(request):
    """
    Context processor to provide menu links for the category app.
    """
    # Fetch all categories to be used in the template context
    links = Category.objects.all()
    return dict(links=links)

