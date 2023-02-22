from django import forms

PRODUCT_QTY_CHOICES = [(i, str(i)) for i in range(1, 21)]
DISCOUNT_CHOICES = [("", "No Discount"), ("25%", "25%"), ("50%", "50%"), ("75%", "75%")]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QTY_CHOICES,
        coerce=int,
        empty_value=1,
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput(),
    )


class CartUpdateProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QTY_CHOICES,
        coerce=int,
        empty_value=1,
        widget=forms.Select(
            attrs={"onchange": "this.form.submit()", "class": "form-control"}
        ),
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput(),
    )
