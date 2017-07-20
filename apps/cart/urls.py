from django.conf.urls import url

from .views import CartAddView


urlpatterns = [
    url(r'(?P<product_id>\d+)/$', CartAddView.as_view(), name='add')
]
