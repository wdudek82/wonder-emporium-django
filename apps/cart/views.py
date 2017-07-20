from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.http import require_POST

from apps.shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


class CartAddView(View):
    def post(self, request, product_id=None):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            cart.add(product=product,
                     quantity=cleaned_data['quantity'],
                     update_quantity=cleaned_data['update'])

        return redirect('cart:cart_detail')


class CartRemoveView(View):
    def get(self, request, product_id=None):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})


# @require_POST
# def cart_add(request, product_id=None):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#
#     if form.is_valid():
#         cleaned_data = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cleaned_data['quantity'],
#                  update_quantity=cleaned_data['update'])
#
#     return redirect('cart:cart_detail')
#
#
# def cart_remove(request, product_id=None):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')
#
#
# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart/cart_detail.html', {'cart': cart})