from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = [
            "product_uid",
            "slug",
            "tags",
            "is_available",
        ]
