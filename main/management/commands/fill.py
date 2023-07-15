from django.core.management import BaseCommand

import json

from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = []
        products_list.append({"title": "Sus Phone ass5",
                              "description": "Super phone",
                              "preview": "",
                              "category": 1,
                              "price": 600000,
                              "date_of_creation": "2023-07-12",
                              "date_of_last_change": "2023-07-12"})

        products_to_fill = []
        for product in products_list:
            products_to_fill.append(Product(**product))

        Product.objects.bulk_create(products_to_fill)

        categories_list = []

        categories_list.append({"title": "Phones",
                                "description": "Everything that can make the call."})

        categories_to_fill = []
        for category in categories_list:
            categories_to_fill.append(Category(**category))

        Category.objects.bulk_create(categories_to_fill)

