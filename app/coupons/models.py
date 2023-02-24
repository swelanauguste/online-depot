from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=200, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(0), MaxLengthValidator(100)],
        help_text="Between 1 to 100 percent",
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
