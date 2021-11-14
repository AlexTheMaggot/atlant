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


class ProductAdmin(PrepopulatedSlug):
    fields = (
        ('name_ru', 'name_uz',),
        'slug',
        ('description_ru', 'description_uz',),
        ('category', 'rent', 'sell',),
        'img_1',
        ('img_2', 'img_3'),
        ('img_4', 'img_5'),
        ('spec_1_ru', 'val_1_ru'),
        ('spec_1_uz', 'val_1_uz'),
        ('spec_2_ru', 'val_2_ru'),
        ('spec_2_uz', 'val_2_uz'),
        ('spec_3_ru', 'val_3_ru'),
        ('spec_3_uz', 'val_3_uz'),
        ('spec_4_ru', 'val_4_ru'),
        ('spec_4_uz', 'val_4_uz'),
        ('spec_5_ru', 'val_5_ru'),
        ('spec_5_uz', 'val_5_uz'),
        ('spec_6_ru', 'val_6_ru'),
        ('spec_6_uz', 'val_6_uz'),
        ('file_1_name_ru', 'file_1_name_uz', 'file_1'),
        ('file_2_name_ru', 'file_2_name_uz', 'file_2'),
        ('file_3_name_ru', 'file_3_name_uz', 'file_3'),
        ('file_4_name_ru', 'file_4_name_uz', 'file_4'),
    )


admin.site.register(Category, PrepopulatedSlug)
admin.site.register(Product, ProductAdmin)
admin.site.register(RentCategory, RentCategoryAdmin)
admin.site.register(RentProduct, PrepopulatedSlug)
