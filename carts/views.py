from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


def cart_add(request):
    product_id = request.POST.get('product_id')

    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.object.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()

        else:
            Cart.object.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_carts(request)

    cart_item_html = render_to_string(
        'carts/includes/included_cart.html', {
            'carts': user_cart
        }, request=request
    )

    response_data = {
        'message': 'Товар добавлен в корзину',
        'cart_item_html': cart_item_html}

    return JsonResponse(response_data)

    # return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass


def cart_remove(request, cart_id):
    cart = Cart.object.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
