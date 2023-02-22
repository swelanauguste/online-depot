# Generated by Django 4.1.6 on 2023-02-09 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="tag_list", to="products.tag"
            ),
        ),
        migrations.AddIndex(
            model_name="category",
            index=models.Index(
                fields=["category_name"], name="products_ca_categor_d63022_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["id", "slug"], name="products_pr_id_a08e3c_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["product_name"], name="products_pr_product_097795_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["-created_at"], name="products_pr_created_bce1a7_idx"
            ),
        ),
    ]
