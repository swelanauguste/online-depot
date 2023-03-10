# Generated by Django 4.1.6 on 2023-02-22 13:00

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_rename_primary_img_product_primary_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("-updated_at",)},
        ),
        migrations.AlterField(
            model_name="product",
            name="primary_image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
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
