from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from account.forms import RegisterUserForm, LoginUserForm
from cart.forms import CartAddProductForm
from .models import Product, Category
from .utils import DataMixin


class ProductCategory(DataMixin, ListView):
    model = Product
    template_name = 'shop/category.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Category", products=context['products'])
        context.update(c_def)
        context['title'] = str(context['products'][0].category)
        return context


def categories(request):
    return HttpResponse('Categories')


def contact(request):
    categories = Category.objects.all()
    context = {'category': categories}
    return render(request, 'shop/contact.html', context)


# def cart(request):
#     return HttpResponse('Cart')


def profile(request):
    return HttpResponse('Profile')


def product_detail(request, product_slug,):
    product = get_object_or_404(Product, slug=product_slug,

                                available=True)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    return render(request,
                  'shop/product.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'category': categories})


# class ShowPost(DataMixin, DetailView, CartAddProductForm):
#     model = Product
#     template_name = 'shop/product.html'
#     slug_url_kwarg = 'product_slug'
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title=context['product'])
#         context.update(c_def)
#
#         return context


class ProductList(DataMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main Page', products=context['products'])
        context.update(c_def)
        return context

    def get_queryset(self):
        return Product.objects.filter(available=True)
