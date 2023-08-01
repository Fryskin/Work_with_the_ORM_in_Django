from django.contrib import admin

from main.models import Product, Category, Version


# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('title',)
    search_fields = ('title', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_number', 'version_title')
    list_filter = ('version_number',)
    search_fields = ('version_number', 'version_title',)