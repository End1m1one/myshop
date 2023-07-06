from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'get_html_photo', 'description', 'stock', 'price', 'available', 'category')
    list_filter = ('price', 'name')
    search_fields = ('name', 'content')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image}' width=60")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
