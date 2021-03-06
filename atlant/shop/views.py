from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from mainapp.views import get_context
from . import models
from mainapp import models as mainapp_models


def product_list(request):
    context = get_context()
    products = models.Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'products': products,
        'page_obj': page_obj,
    })
    if '/uz/' in request.path:
        template = 'shop/product_list_uz.html'
    else:
        template = 'shop/product_list.html'
    return render(request, template, context)


def category_detail(request, category_slug):
    context = get_context()
    category = get_object_or_404(models.Category, slug=category_slug)
    products = models.Product.objects.all().filter(category_id=category.id)
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'category': category,
        'products': products,
        'page_obj': page_obj,
    })
    if '/uz/' in request.path:
        template = 'shop/category_detail_uz.html'
    else:
        template = 'shop/category_detail.html'
    return render(request, template, context)


def product_detail(request, category_slug, product_slug):
    context = get_context()
    product = get_object_or_404(models.Product, slug=product_slug)
    category = get_object_or_404(models.Category, slug=category_slug)
    context.update({
        'category': category,
        'product': product,
    })
    if '/uz/' in request.path:
        template = 'shop/product_detail_uz.html'
    else:
        template = 'shop/product_detail.html'
    return render(request, template, context)


def search(request):
    context = get_context()
    if '/uz/' in request.path:
        search_categories = models.Category.objects.all().filter(name_uz__icontains=request.GET.get('search'))
        search_products = models.Product.objects.all().filter(name_uz__icontains=request.GET.get('search'))
        search_rent_products = models.RentProduct.objects.all().filter(name_uz__icontains=request.GET.get('search'))
    else:
        search_categories = models.Category.objects.all().filter(name_ru__icontains=request.GET.get('search'))
        search_products = models.Product.objects.all().filter(name_ru__icontains=request.GET.get('search'))
        search_rent_products = models.RentProduct.objects.all().filter(name_ru__icontains=request.GET.get('search'))
    paginator = Paginator(search_products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    rent_paginator = Paginator(search_rent_products, 8)
    rent_page_number = request.GET.get('rent_page')
    rent_page_obj = rent_paginator.get_page(rent_page_number)
    context.update({
        'search_categories': search_categories,
        'search_products': search_products,
        'page_obj': page_obj,
        'rent_page_obj': rent_page_obj,
    })
    if '/uz/' in request.path:
        template = 'shop/search_uz.html'
    else:
        template = 'shop/search.html'
    return render(request, template, context)


def rent_category_detail(request, rent_category_slug):
    context = get_context()
    rent_category = get_object_or_404(models.RentCategory, slug=rent_category_slug)
    rent_products = models.RentProduct.objects.all().filter(category__slug=rent_category_slug)
    paginator = Paginator(rent_products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'rent_category': rent_category,
        'page_obj': page_obj,
    })
    if '/uz/' in request.path:
        template = 'shop/rent_category_detail_uz.html'
    else:
        template = 'shop/rent_category_detail.html'
    return render(request, template, context)


def rent_product_detail(request, rent_category_slug, rent_product_slug):
    context = get_context()
    rent_category = get_object_or_404(models.RentCategory, slug=rent_category_slug)
    rent_product = get_object_or_404(models.RentProduct, slug=rent_product_slug)
    context.update({
        'rent_category': rent_category,
        'rent_product': rent_product,
    })
    if '/uz/' in request.path:
        template = 'shop/rent_product_detail_uz.html'
    else:
        template = 'shop/rent_product_detail.html'
    return render(request, template, context)