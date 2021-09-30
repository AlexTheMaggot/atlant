from django.urls import path
from . import views
from shop import views as shop_views

app_name = 'mainapp'

urlpatterns = [
    # Ru
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rent-terms/', views.rent_terms, name='rent_terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('services/', views.services, name='services'),
    path('catalog/', shop_views.product_list, name='product_list'),
    # End Ru
    # Uz
    path('uz/', views.index, name='index_uz'),
    path('uz/about/', views.about, name='about_uz'),
    path('uz/rent-terms/', views.rent_terms, name='rent_terms_uz'),
    path('uz/contacts/', views.contacts, name='contacts_uz'),
    path('uz/delivery/', views.delivery, name='delivery_uz'),
    path('uz/services/', views.services, name='services_uz'),
    # End Uz
]



