from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'category/(?P<category_id>\d+)/$', ProductsListByCategoryView, name='product_list_by_category'),
    url(r'product/(?P<product_id>\d+)/$', ProductDetailView, name='product_detail'),
]
