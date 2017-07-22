from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from .models import Category, Product
from apps.cart.forms import CartAddProductForm


class ProductListView(View):
    def get(self, request):
        products = Product.objects.filter(available=True).order_by('id')
        return render(request, 'shop/product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, product_id=None):
        product = get_object_or_404(Product, id=product_id)
        cart_product_form = CartAddProductForm

        context = {
            'product': product,
            'cart_product_form': cart_product_form
        }

        return render(request, 'shop/product_detail.html', context)


class ProductListByCategoryView(View):
    def get(self, request, category_id=None):
        products = Product.objects.filter(category=category_id, available=True)
        return render(request, 'shop/product_list_by_category.html', {'products': products})
