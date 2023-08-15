from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'мобильные телефоны', 'description': 'интересные новинки и флагманские смартфоны'},
            {'name': 'ПК и ноутбуки', 'description': 'лучшее для дома и работы'},
            {'name': 'оргтехника', 'description': 'МФУ, принтеры и сканеры для широкого применения'},
            {'name': 'комплектующие',
             'description': 'железо, системы охлаждения, звуковые карты, корпуса для вашего компьютера'},
            {'name': 'компьютерная акустика', 'description': 'колонки и гарнитуры для компьютера'}
        ]

    category_for_create = []
    for category_item in category_list:
        category_for_create.append(
            Category(**category_item)
        )

    Category.objects.bulk.create(category_for_create)
