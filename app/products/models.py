import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

Owner = settings.AUTH_USER_MODEL


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ("category_name",)
        verbose_name_plural = "categories"
        verbose_name = "category"
        indexes = [
            models.Index(fields=["category_name"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        ordering = ("tag_name",)
        indexes = [
            models.Index(fields=["tag_name"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.tag_name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.tag_name


class Product(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255, unique=True)
    product_uid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, blank=True, null=True
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(
        Category, related_name="category_list", on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(Tag, related_name="tag_list", blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    primary_image = models.FileField(upload_to="primary_images", default="default.jpg")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("product_name",)
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["product_name"]),
            models.Index(fields=["-created_at"]),
        ]

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # Newly created object, so set slug
            self.slug = slugify(self.product_uid)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_image_list", on_delete=models.CASCADE
    )
    image = models.FileField(upload_to="product_images", blank=True)

    def __str__(self):
        return self.product.product_name


# class ProductVariationManager(models.Manager):
#     def all(self, *args, **kwargs):
#         qs_main = super(ProductVariationManager, self).filter(main=True)

# class Cart(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ("created_at",)
#         verbose_name_plural = "carts"
#         verbose_name = "cart"
#         indexes = [models.Index(fields=["created_at"]),]

#     def __str__(self):
#         return str(self.user)


# class CartItem(models.Model):
#     product = models.ForeignKey(Product, related_name="cart_items", on
