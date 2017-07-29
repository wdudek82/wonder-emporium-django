from django.db import models
from django.contrib.auth.models import User
from apps.shop.models import Product


class Order(models.Model):
    client = models.ForeignKey(User, related_name='orders')
    product = models.ForeignKey(Product, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
