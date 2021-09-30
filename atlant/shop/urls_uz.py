from django.urls import path
from . import views

app_name = 'catalog_uz'

urlpatterns = [
    path('', views.product_list, name='product_list_uz'),
    path('<slug:category_slug>/', views.category_detail, name='category_detail_uz'),
]