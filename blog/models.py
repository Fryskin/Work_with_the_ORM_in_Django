from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='title')
    slug = models.CharField(max_length=50, verbose_name='slug')
    content = models.TextField(verbose_name='content')
    preview = models.ImageField(upload_to='products/', verbose_name='preview', **NULLABLE)
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='date of creation')
    is_published = models.BooleanField(default=True, verbose_name='publish status')
    count_of_views = models.PositiveIntegerField(default=0, verbose_name='count of views', editable=False)

    def __str__(self):
        return f'{self.title}.'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ('title',)

