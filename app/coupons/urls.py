from django.urls import path

from .views import coupon_apply_view


urlpatterns = [
    path('apply/', coupon_apply_view, name='coupon-apply'),
]
