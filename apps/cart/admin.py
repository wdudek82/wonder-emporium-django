from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'price', 'quantity', 'session']
    list_display_links = ['product']
