from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'category/(?P<category_id>\d+)/$', ProductsListByCategoryView.as_view(), name='product_list_by_category'),
    url(r'product/(?P<product_id>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
]