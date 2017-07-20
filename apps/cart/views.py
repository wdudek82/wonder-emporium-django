from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.shop.models import Product
from .cart import Cart
from .forms import CartAddProductFrom


@require_POST
def add_product_to_cart(request, product_id=None):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductFrom(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product=product,
                 quantity=cleaned_data['quantity'],
                 update_quantity=cleaned_data['updata'])

    return redirect('cart:cart_detail')
