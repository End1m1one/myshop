from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from django.http import JsonResponse

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity']
        cart.add(product=product, quantity=quantity, override_quantity=cd['override'])

    # Recalculate the total price after updating the quantity
    total_price = cart.get_total_price()

    total_items = len(cart)

    # Return the response as JSON
    response_data = {
        'total_price': total_price,
        'total_items': total_items,
    }

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse(response_data)
    else:
        return redirect('cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    total_items = len(cart)  # Calculate the total items count
    categories = Category.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
        item['update_quantity_form'].fields['quantity'].widget.attrs.update({
            'data-product-id': item['product']})

    context = {
        'category': categories,
        'cart': cart,
        'title': 'Your Cart',
        'total_items': total_items,  # Pass the total items count to the template
    }
    return render(request, 'cart/cart.html', context=context)
