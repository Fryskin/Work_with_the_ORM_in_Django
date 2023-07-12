from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.CharField(max_length=100, verbose_name='description')
    preview = models.ImageField(upload_to='products/', verbose_name='preview', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='category')
    price = models.IntegerField(verbose_name='price')
    date_of_creation = models.DateField(verbose_name='date_of_creation')
    date_of_last_change = models.DateField(verbose_name='date_of_last_change')

    def __str__(self):
        return f'{self.title},{self.description}, {self.category}, {self.price},' \
               f' {self.date_of_creation}, {self.date_of_last_change}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('title',)


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.CharField(max_length=100, verbose_name='description')

    def __str__(self):
        return f'{self.title}, {self.description}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('title',)

