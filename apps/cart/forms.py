from django import forms
from apps.shop.models import Product




class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

    # def __init__(self, data=None, *args, **kwargs):
    #     super(CartAddProductForm, self).__init__(data, *args, **kwargs)
    #     print(self.__dict__)
    #     print('===', self.renderer.__dict__)
    #     print(data)
    #     print(*args)
    #     print(**kwargs)

