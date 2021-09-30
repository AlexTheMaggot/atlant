from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from . import models


class SingleElementModelConfig(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ContactPageAdmin(SingleElementModelConfig):
    fields = (
        (
            'phone_title_1_ru',
            'phone_title_1_uz',
            'phone_1',
        ),
        (
            'phone_title_2_ru',
            'phone_title_2_uz',
            'phone_2',
        ),
        (
            'phone_title_3_ru',
            'phone_title_3_uz',
            'phone_3',
        ),
        (
            'phone_title_4_ru',
            'phone_title_4_uz',
            'phone_4',
        ),
        (
            'phone_title_5_ru',
            'phone_title_5_uz',
            'phone_5',
        ),
        (
            'mail_title_1_ru',
            'mail_title_1_uz',
            'mail_1',
        ),
        (
            'mail_title_2_ru',
            'mail_title_2_uz',
            'mail_2',
        ),
        (
            'mail_title_3_ru',
            'mail_title_3_uz',
            'mail_3',
        ),
        (
            'mail_title_4_ru',
            'mail_title_4_uz',
            'mail_4',
        ),
        (
            'mail_title_5_ru',
            'mail_title_5_uz',
            'mail_5',
        ),
        (
            'address_title_1_ru',
            'address_title_1_uz',
            'address_1_ru',
            'address_1_uz',
        ),
        (
            'address_title_2_ru',
            'address_title_2_uz',
            'address_2_ru',
            'address_2_uz',
        ),
        (
            'address_title_3_ru',
            'address_title_3_uz',
            'address_3_ru',
            'address_3_uz',
        ),
        (
            'address_title_4_ru',
            'address_title_4_uz',
            'address_4_ru',
            'address_4_uz',
        ),
        (
            'address_title_5_ru',
            'address_title_5_uz',
            'address_5_ru',
            'address_5_uz',
        ),
        (
            'callback_text_ru',
            'callback_text_uz',
        ),
    )


class DeliveryPageAdmin(SummernoteModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    summernote_fields = ('text_ru', 'text_uz')


class MainPageAdmin(SingleElementModelConfig):
    fields = (
        (
            'first_block_title_ru',
            'first_block_description_ru',
            'first_block_title_uz',
            'first_block_description_uz',
        ),
        (

        ),
        (
            'about_par_1_ru',
            'about_par_2_ru',
            'about_par_1_uz',
            'about_par_2_uz',
        ),
        'about_img',
        (
            'client',
            'sold',
            'success',
        ),
    )


class AboutPageAdmin(SingleElementModelConfig):
    fields = (
        (
        'text_1_ru',
        'text_2_ru',
        ),
        (
        'text_1_uz',
        'text_2_uz',
        ),
        (
        'year',
        'order',
        'delivery',
        'repeated',
        ),
    )


admin.site.register(models.Header, SingleElementModelConfig)
admin.site.register(models.Footer, SingleElementModelConfig)
admin.site.register(models.MainPage, MainPageAdmin)
admin.site.register(models.ContactPage, ContactPageAdmin)
admin.site.register(models.RentTermPage, SingleElementModelConfig)
admin.site.register(models.DeliveryPage, DeliveryPageAdmin)
admin.site.register(models.AboutPage, AboutPageAdmin)
admin.site.register(models.WorkSteps)
admin.site.register(models.Reviews)
admin.site.register(models.Partner)
admin.site.register(models.Service)
