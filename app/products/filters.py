import django_filters
from django import forms

from .models import Category, Product, Tag


class ProductFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Name",
        widget=forms.TextInput(attrs={"class": "rounded-pill"}),
    )
    # category__category_name = django_filters.CharFilter(
    #     queryset=Category.objects.all(),
    #     lookup_expr="icontains",
    #     label="Category",
    #     widget=forms.TextInput(attrs={"class": "rounded-pill"}),
    # )

    # category = django_filters.ModelChoiceFilter(
    #     queryset=Category.objects.all(),
    #     widget=forms.Select(attrs={"class": "rounded-pill"}),
    # )
    category__category_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="category",
        widget=forms.TextInput(attrs={"class": "rounded-pill"}),
    )
    tags__tag_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="tags",
        widget=forms.TextInput(attrs={"class": "rounded-pill"}),
    )

    class Meta:
        model = Product
        fields = ("product_name", "category__category_name", "tags__tag_name")
