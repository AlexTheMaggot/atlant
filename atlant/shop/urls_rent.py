from django.urls import path
from . import views

app_name = 'rent'

urlpatterns = [
    path('<slug:rent_category_slug>/', views.rent_category_detail, name='rent_category_detail'),
    path('<slug:rent_category_slug>/<slug:rent_product_slug>/', views.rent_product_detail,
         name='rent_product_detail'),
]