import json

from django.core.management import BaseCommand

import os

from main.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        os.system('python manage.py loaddata data_to_fill.json')



