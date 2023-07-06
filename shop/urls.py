from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('categories/', categories, name='categories'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile'),
    path('product/<slug:product_slug>/', product_detail, name='product'),
    path('category/<slug:category_slug>/', ProductCategory.as_view(), name='category')
]