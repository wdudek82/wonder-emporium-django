from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description', 'category', 'get_image', 'price', 'stock', 'available',
                    'created', 'updated']
    list_display_links = ['name']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, instance):
        image = instance.image
        return mark_safe('<img src ="{}">'.format(image.url)) if image else '-'
    get_image.short_description = 'image'

