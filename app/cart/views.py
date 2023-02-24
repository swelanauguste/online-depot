from coupons.forms import CouponApplyForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from products.models import Product

from .cart import Cart
from .forms import CartAddProductForm, CartUpdateProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("cart-detail")


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart-detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item["update_quantity_form"] = CartUpdateProductForm(
            initial={"quantity": item["quantity"], "update": True}
        )
    coupon_apply_form = CouponApplyForm()
    context = {"cart": cart, "coupon_apply_form": coupon_apply_form}
    return render(request, "cart/cart_detail.html", context)
