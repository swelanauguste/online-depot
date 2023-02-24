import uuid
from decimal import Decimal

from coupons.models import Coupon
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify
from products.models import Product


class Location(models.Model):
    location = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.location.title()


class Order(models.Model):
    order_uid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        Coupon, related_name="orders", null=True, blank=True, on_delete=models.SET_NULL
    )
    discount = models.CharField(
        max_length=3,
        default=0,
        validators=[MinLengthValidator(0), MaxLengthValidator(100)],
    )

    class Meta:
        ordering = ("-created_at",)
        indexes = [
            models.Index(
                fields=[
                    "created_at",
                ]
            ),
        ]

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.order_uid)
        super(Order, self).save(*args, **kwargs)

    def get_total_cost(self):
        total_cost = self.get_total_cost_before_discount()
        return total_cost - self.get_discount()

    def get_total_cost_before_discount(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_discount(self):
        total_cost = self.get_total_cost_before_discount()
        if self.discount:
            return total_cost * ((Decimal(int(self.discount))) / Decimal(100))
        return Decimal(0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity
