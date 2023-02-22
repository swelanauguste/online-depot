from decimal import Decimal
from random import randint, randrange

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category, Product, Tag

Owners = get_user_model()


# yr_cls_count = YearClass.objects.count()
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(100):
            owner = Owners.objects.get(pk=1)
            product_name = fake.sentence(nb_words=5)
            category = Category.objects.get(pk=randint(1, Category.objects.count()))
            description = fake.sentence(nb_words=13)
            price = Decimal(randrange(2000, 38900)) / 100
            Product.objects.get_or_create(
                owner=owner,
                product_name=product_name,
                category=category,
                description=description,
                price=price,
            )
            self.stdout.write(self.style.SUCCESS(f"{product_name}"))
