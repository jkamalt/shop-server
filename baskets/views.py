from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse

from products.models import Product
from baskets.models import Basket


@login_required
def basket_add(request, product_id):
    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)

        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            is_success = basket.set_basket_quantity(basket.quantity + 1)
            basket.save()

            if not is_success:
                messages.error(request, f'Невозможно добавить товар {product.name}. Превышен остаток на складе: {product.quantity}')

    return JsonResponse({})


@login_required
def basket_remove(request, id):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        basket.delete()
    return JsonResponse({'result': create_baskets_string_render(request)})


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.set_basket_quantity(quantity)
            basket.save()
        else:
            basket.delete()
    return JsonResponse({'result': create_baskets_string_render(request)})


def create_baskets_string_render(request):
    baskets = Basket.objects.filter(user=request.user)
    context = {'baskets': baskets}
    return render_to_string('baskets/baskets.html', context)
