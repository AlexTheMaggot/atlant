from django.urls import path
from . import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rent-terms/', views.rent_terms, name='rent_terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('services/', views.services, name='services'),
    path('callback_send/', views.callback_send, name='callback_send'),
    path('another_callback_send/', views.another_callback_send, name='another_callback_send'),
    path('one_more_callback_send/', views.one_more_callback_send, name='one_more_callback_send'),
    path('rent_order/', views.rent_order, name='rent_order'),
    path('not_found_send/', views.not_found_send, name='not_found_send'),
    path('product_order/', views.product_order, name='product_order'),
    path('service_order/', views.service_order, name='service_order'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
