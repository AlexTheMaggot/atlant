from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from mainapp.views import context
from . import models
from mainapp import models as mainapp_models


def product_list(request):
    reviews = mainapp_models.Reviews.objects.all()
    products = models.Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'products': products,
        'page_obj': page_obj,
        'reviews': reviews,
    })
    if '/uz/' in request.path:
        template = 'shop/product_list_uz.html'
    else:
        template = 'shop/product_list.html'
    return render(request, template, context)


def category_detail(request, category_slug):
    reviews = mainapp_models.Reviews.objects.all()
    category = get_object_or_404(models.Category, slug=category_slug)
    products = models.Product.objects.all().filter(category_id=category.id)
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'category': category,
        'products': products,
        'page_obj': page_obj,
        'reviews': reviews,
    })
    if '/uz/' in request.path:
        template = 'shop/category_detail_uz.html'
    else:
        template = 'shop/category_detail.html'
    return render(request, template, context)


def product_detail(request, category_slug, product_slug):
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
    search_categories = models.Category.objects.all().filter(name_ru__icontains=request.GET.get('search'))
    products = models.Product.objects.all().filter(name_ru__icontains=request.GET.get('search'))
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'search_categories': search_categories,
        'products': products,
        'page_obj': page_obj,
    })
    if '/uz/' in request.path:
        template = 'shop/search_uz.html'
    else:
        template = 'shop/search.html'
    return render(request, template, context)
