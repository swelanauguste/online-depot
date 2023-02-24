# Generated by Django 4.1.6 on 2023-02-22 13:06

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_product_options_alter_product_primary_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="primary_image",
            field=django_resized.forms.ResizedImageField(
                crop=["middle", "center"],
                default="default.jpg",
                force_format=None,
                keep_meta=True,
                quality=-1,
                scale=None,
                size=[640, 425],
                upload_to="primary_images",
            ),
        ),
    ]