from django.urls import path

from .views import ProductDetailView, ProductListView, product_create_form

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('add-product/', product_create_form, name='product-create'),
    path('detail/<slug:slug>', ProductDetailView.as_view(), name='product-detail'),

]
