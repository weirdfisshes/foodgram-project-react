from csv import reader

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


SIZE_OF_ROW = 2


class Command(BaseCommand):
    help = 'Load ingredients data from csv-file to DB.'

    def handle(self, *args, **kwargs):
        with open(
                'recipes/data/ingredients.csv', 'r',
                encoding='UTF-8'
        ) as ingredients:
            for row in reader(ingredients):
                if len(row) == SIZE_OF_ROW:
                    Ingredient.objects.get_or_create(
                        name=row[0], unit=row[1],
                    )
