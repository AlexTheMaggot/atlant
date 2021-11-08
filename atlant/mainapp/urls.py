from django.urls import path
from . import views
from shop import views as shop_views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rent-terms/', views.rent_terms, name='rent_terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('services/', views.services, name='services'),
]
