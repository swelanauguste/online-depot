import weasyprint
from cart.cart import Cart
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .forms import OrderCreateForm
from .models import Order, OrderItem
from .tasks import order_created


@staff_member_required
def admin_member_pdf(request, order_id):
    order = Order.objects.get(id=order_id)
    html = render_to_string("orders/pdf.html", {"order": order})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"filename=order_{order.order_uid}.pdf"
    weasyprint.HTML(string=html).write_pdf(
        response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    )
    return response


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            order_created.delay(order.id)
        return render(request, "orders/order_created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "orders/order_create.html", {"cart": cart, "form": form})
