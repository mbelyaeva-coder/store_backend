from django.contrib import admin
from django.utils.html import format_html

from store import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'store', 'quantity_in_stock', 'category']
    list_per_page = 10
    list_editable = ['title', 'price', 'store', 'quantity_in_stock', 'category']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_per_page = 10
    list_editable = ['title', ]


class StoreImageInline(admin.TabularInline):
    model = models.StoreImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, obj):
        if obj.image.name !='':
            return format_html(f'<img src="{obj.image.url}" class="thumbnail" />')
        return ''


@admin.register(models.Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [StoreImageInline]
    list_display = ['id', 'title']
    list_per_page = 10
    list_editable = ['title', ]
    search_fields = ['title']

    class Media:
        css = {'all': ['store/styles.css']}
