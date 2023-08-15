from django.core.management import BaseCommand
import json
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        with open('data.json') as file:
            data = json.load(file)

        for item in data:
            category = Category(name=item['name'])
            category.save()
