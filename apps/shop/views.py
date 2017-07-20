from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from .models import Category, Product


class ProductListView(View):
    def get(self, request):
        products = Product.objects.filter(available=True).order_by('id')
        return render(request, 'shop/product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, product_id=None):
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'shop/product_detail.html', {'product': product})


class ProductListByCategoryView(View):
    def get(self, request, category_id=None):
        products = Product.objects.filter(category=category_id, available=True)
        return render(request, 'shop/product_list_by_category.html', {'products': products})
