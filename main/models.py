from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    description = models.CharField(max_length=1000, verbose_name='description')
    preview = models.ImageField(upload_to='products/', verbose_name='preview', **NULLABLE)
    category = models.ForeignKey('Category', verbose_name='category', on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name='price')
    date_of_creation = models.DateField(verbose_name='date_of_creation')
    date_of_last_change = models.DateField(verbose_name='date_of_last_change')
    is_published = models.BooleanField(default=False, verbose_name='publish status', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='owner')

    def __str__(self):
        return f'{self.title}, {self.description}, {self.category}, {self.price},' \
               f' {self.date_of_creation}, {self.date_of_last_change}, {self.owner}'

    class Meta:

        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title',)

        permissions = [
            (
                "can_edit_product",
                "Can Edit Product"
            )
        ]


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    description = models.CharField(max_length=1000, verbose_name='description')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)


class Version(models.Model):
    product = models.ForeignKey('Product', verbose_name='product', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='version number')
    version_title = models.CharField(max_length=150, verbose_name='version title')
    is_version_valid = models.BooleanField(verbose_name='is version valid')

    def __str__(self):
        return f'{self.version_title}, {self.version_number}'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
        ordering = ('version_number',)
