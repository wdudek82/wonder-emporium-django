from django.conf.urls import url

from .views import CartAddView, CartDetailView, CartRemoveView


urlpatterns = [
    url(r'^$', CartDetailView.as_view(), name='detail'),
    url(r'add/(?P<product_id>\d+)/$', CartAddView.as_view(), name='add'),
    url(r'remove/(?P<product_id>\d+)/$', CartRemoveView.as_view(), name='remove')
]
