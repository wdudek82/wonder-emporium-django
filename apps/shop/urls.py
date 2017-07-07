from django.conf.urls import url
from .views import (product_detail_view, product_list_view, product_list_by_category_view,
                    ProductDetailView, ProductListByCategoryView)


urlpatterns = [
    url(r'products/$', product_list_view, name='product_list'),
    url(r'product/(?P<product_id>\d+)/$', product_detail_view, name='product_detail'),
    url(r'products/category/(?P<category_id>\d+)/$', product_list_by_category_view, name='product_list_by_category'),

    url(r'cbv/products/category/(?P<category_id>\d+)/$', ProductListByCategoryView, name='cbv_product_list_by_category'),
    url(r'cbv/product/(?P<product_id>\d+)/$', ProductDetailView, name='cbv_product_detail'),
]
