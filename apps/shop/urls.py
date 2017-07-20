from django.conf.urls import url
from .views import ProductDetailView, ProductListView, ProductListByCategoryView


urlpatterns = [
    url(r'products/$', ProductListView.as_view(), name='product_list'),
    url(r'product/(?P<product_id>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'product/category/(?P<category_id>\d+)/$',
        ProductListByCategoryView.as_view(), name='product_list_by_category'),
]
