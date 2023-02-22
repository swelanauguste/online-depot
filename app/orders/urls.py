from django.urls import path

from .views import admin_member_pdf, order_create

urlpatterns = [
    path("create/", order_create, name="order-create"),
    path("admin/order/<int:order_id>/pdf/", admin_member_pdf, name="order_pdf"),
]
