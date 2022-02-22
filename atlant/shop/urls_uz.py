from django.urls import path
from . import views

app_name = 'catalog_uz'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail'),
]