from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'description', 'image')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name',)
    list_filter = ('category_name',)
    ordering = ('category_name',)

admin.site.register(Category, CategoryAdmin)

