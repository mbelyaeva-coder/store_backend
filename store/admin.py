from django.contrib import admin

from store import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'store', 'quantity_in_stock', 'category')
    list_per_page = 10
    list_editable = ('title', 'price', 'store', 'quantity_in_stock', 'category')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 10
    list_editable = ('title', )


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_per_page = 10
    list_editable = ('title', )