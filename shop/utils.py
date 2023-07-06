from itertools import zip_longest

from cart.forms import CartAddProductForm
from shop.models import Category


class DataMixin:
    paginate_by = 4
    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.all()
        cart_product_form = CartAddProductForm
        context['category'] = category
        context['cart_prodcut_form']= cart_product_form
        if 'products' in context:
            products = context['products']
            rows = list(zip_longest(*(iter(products),) * 4))
            context['product_rows'] = rows
        return context