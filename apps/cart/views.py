from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.sessions.models import Session
from django.views import View

from apps.shop.models import Product
from .models import Cart
from .forms import CartAddProductForm


class CartAddView(View):
    def post(self, request, product_id=None):
        session = Session.objects.get(session_key=request.session._SessionBase__session_key)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            cart, created = Cart.objects.get_or_create(product=product, price=product.price, session=session)

            quantity = cleaned_data['quantity']
            update_quantity = cleaned_data['update']
            if update_quantity:
                cart.quantity = quantity
            else:
                cart.quantity += quantity

            cart.save()

        return redirect('shop:product_list')


class CartRemoveView(View):
    def get(self, request, product_id=None):
        session_key = request.session._SessionBase__session_key
        cart = Cart.objects.filter(session=session_key)

        for cart_item in cart:
            product = cart_item.product
            if product.id == int(product_id):
                cart_item.delete()

        # return redirect('cart:cart_detail')
        return redirect('shop:product_list')


class CartDetailView(View):
    def get(self, request):
        session_key = request.session._SessionBase__session_key
        cart = Cart.objects.filter(session=session_key)
        return render(request, 'cart/cart_detail.html', {'cart': cart})


# TODO: Add missing html template
# TODO: Make those templates pretty;)
# TODO: Add custom context manager for cart or custom template tag (e.g. to show cart short info in page header)
# TODO: Disallow selecting more items than there is in stock
# TODO: Add tests functional and unit tests!