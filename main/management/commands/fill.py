from django.core.management import BaseCommand

import json

from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = "product_data.json"

        with open(path) as json_file:
            content = json.load(json_file)
            json_file.close()
            products_list = []
            for product in content:
                products_list.append({'title': product['fields']['title'],
                                      'description': product['fields']['description'],
                                      'preview': product['fields']['preview'],
                                      'category': product['fields']['category'],
                                      'price': product['fields']['price'],
                                      'date_of_creation': product['fields']['date_of_creation'],
                                      'date_of_last_change': product['fields']['date_of_last_change']})

        products_to_fill = []
        for product in products_list:
            products_to_fill.append(Product(**product))

        Product.objects.bulk_create(products_to_fill)

        # path_2 = "category_data.json"
        #
        # with open(path_2) as json_file_2:
        #     content = json.load(json_file_2)
        #     json_file_2.close()
        #
        #     categories_list = []
        #     for category in content:
        #         categories_list.append({'title': category['fields']['title'],
        #                                 'description': category['fields']['description']
        #                                 })
        #
        # categories_to_fill = []
        # for category in categories_list:
        #     categories_to_fill.append(Category(**category))
        #
        # Category.objects.bulk_create(categories_to_fill)

