from django.core.management.base import BaseCommand

from ...models import Location


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/location_list.txt") as file:
            for row in file:
                location = row.replace("\n", "")
                Location.objects.get_or_create(
                    location=location,
                )
                self.stdout.write(self.style.SUCCESS(f"{location} added"))
                