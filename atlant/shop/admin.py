from django.contrib import admin
from . models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name_ru',),
    }


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name_ru',),
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
