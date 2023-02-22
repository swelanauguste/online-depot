from django.core.management.base import BaseCommand

from ...models import Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/category_list.txt") as file:
            for row in file:
                category_name = row.replace("\n", "")
                Category.objects.get_or_create(
                    category_name=category_name,
                )
                self.stdout.write(self.style.SUCCESS(f"{category_name} added"))
                