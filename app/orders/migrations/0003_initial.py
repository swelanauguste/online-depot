# Generated by Django 4.1.6 on 2023-02-10 21:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0003_rename_primary_img_product_primary_image"),
        ("orders", "0002_remove_orderitem_order_remove_orderitem_product_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order_uid",
                    models.UUIDField(
                        blank=True,
                        default=uuid.uuid4,
                        editable=False,
                        null=True,
                        unique=True,
                    ),
                ),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=250)),
                ("location", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("paid", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["created_at"], name="orders_orde_created_0e92de_idx"
            ),
        ),
    ]