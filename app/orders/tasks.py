from celery import shared_task
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage, send_mail

from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    current_site = Site.objects.get_current()
    addr = current_site.domain
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name},\n\nYour order was placed and your order ID is {order.order_uid}. \n\nThank you from {addr}"
    mail_sent = send_mail(subject, message, "kingship.lc@gmail.com", [order.email])
    return mail_sent
