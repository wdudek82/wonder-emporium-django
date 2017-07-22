from django.utils.text import slugify

from faker import Factory
# from apps.shop.models import Category, Product


fake = Factory.create()

product_categories = [
    'diet',
    'electronics',
    'fashion',
    'health',
    'home',
    'sport',
]

for _ in range(10):
    name = fake.words()
    print(name)