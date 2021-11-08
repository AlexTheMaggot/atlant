from django.contrib import admin
from . models import Category, Product, RentCategory, RentProduct


class PrepopulatedSlug(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name_ru',),
    }


class RentCategoryAdmin(PrepopulatedSlug):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Category, PrepopulatedSlug)
admin.site.register(Product, PrepopulatedSlug)
admin.site.register(RentCategory, RentCategoryAdmin)
admin.site.register(RentProduct, PrepopulatedSlug)
