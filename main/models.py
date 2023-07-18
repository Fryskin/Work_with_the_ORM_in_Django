from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    description = models.CharField(max_length=100, verbose_name='description')
    preview = models.ImageField(upload_to='products/', verbose_name='preview', **NULLABLE)
    category = models.ForeignKey('Category', verbose_name='category', on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name='price')
    date_of_creation = models.DateField(verbose_name='date_of_creation')
    date_of_last_change = models.DateField(verbose_name='date_of_last_change')

    def __str__(self):
        return f'{self.title}, {self.description}, {self.category}, {self.price},' \
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


class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='title')
    slug = models.SlugField(primary_key=True, max_length=250, unique=True, default='')
    body = models.TextField(verbose_name='content')
    preview = models.ImageField(upload_to='products/', verbose_name='preview', **NULLABLE)
    date_of_creation = models.DateField(verbose_name='date of creation')
    count_of_views = models.IntegerField(verbose_name='count of views')

    def __str__(self):
        return f'{self.title}, {self.slug}, {self.body}, {self.preview}, {self.date_of_creation}, {self.count_of_views}'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

