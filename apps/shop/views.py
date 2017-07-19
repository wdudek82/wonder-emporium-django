from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Category, Product


def product_list_view(request):
    products = Product.objects.filter(available=True).order_by('id')

    context = {
        'products': products,
    }

    return render(request, 'shop/product_list.html', context)


def product_detail_view(request, product_id=None):
    product = get_object_or_404(Product, id=product_id, available=True)

    context = {
        'product': product,
    }
    return render(request, 'shop/product_detail.html', context)


def product_list_by_category_view(request, category_id=None):
    products = Product.objects.filter(category=category_id, available=True)

    context = {
        'products': products,
    }
    return render(request, 'shop/product_list_by_category.html', context)


def add_product_to_cart(request, user_id=None):
    user = get_object_or_404(User, id=user_id)

    context = {
        'cart': request.session
    }
    return render(request, 'shop/user_cart.html', context)


class ProductListByCategoryView:
    pass


class ProductDetailView:
    pass
