from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from apps.cart.models import Cart


def order_create(request):
    cart = Cart(request)
    return render(request, '', {})