from django.core.management.base import BaseCommand

from ...models import Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/tag_list.txt") as file:
            for row in file:
                tag_name = row.replace("\n", "")
                Tag.objects.get_or_create(
                    tag_name=tag_name,
                )
                self.stdout.write(self.style.SUCCESS(f"{tag_name} added"))
                