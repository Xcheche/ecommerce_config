from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
import store.models as models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'slug')
    list_filter = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'category',
        'title',
        'slug',
        'image',
        'description',
        'price',
        'discount',
        'available',
        "slug",
    )
    list_filter = (
        'category',
        'available',
        'id',
        'title',
        'slug',
        'image',
        'description',
        'price',
        'discount',
    )
    search_fields = ('slug',)
    prepopulated_fields = {'slug': ['title']}


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Product, ProductAdmin)
