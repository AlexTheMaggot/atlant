from django.shortcuts import render
from django.core.paginator import Paginator
from . import models
from shop.models import Category, Product, RentCategory, RentProduct


def get_context():
    header = models.Header.objects.first()
    footer = models.Footer.objects.first()
    categories = Category.objects.all()
    rent_categories = RentCategory.objects.all()
    context = {
        'header': header,
        'footer': footer,
        'categories': categories,
        'rent_categories': rent_categories,
    }
    return context


def index(request):
    context = get_context()
    main_page = models.MainPage.objects.first()
    reviews = models.Reviews.objects.all()
    partners = models.Partner.objects.all()
    worksteps = models.WorkSteps.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(1)
    context.update({
        'main_page': main_page,
        'reviews': reviews,
        'partners': partners,
        'worksteps': worksteps,
        'page_obj': page_obj,
    })
    if '/uz/' in request.path:
        template = 'mainapp/index_uz.html'
    else:
        template = 'mainapp/index.html'
    return render(request, template, context)


def about(request):
    context = get_context()
    partners = models.Partner.objects.all()
    reviews = models.Reviews.objects.all()
    about_page = models.AboutPage.objects.first()
    context.update({
        'reviews': reviews,
        'partners': partners,
        'about_page': about_page,
    })
    if '/uz/' in request.path:
        template = 'mainapp/about_uz.html'
    else:
        template = 'mainapp/about.html'
    return render(request, template, context)


def rent_terms(request):
    context = get_context()
    rent_terms_page = models.RentTermPage.objects.first()
    reviews = models.Reviews.objects.all()
    context.update({
        'reviews': reviews,
        'rent_terms_page': rent_terms_page,
    })
    if '/uz/' in request.path:
        template = 'mainapp/rent_terms_uz.html'
    else:
        template = 'mainapp/rent_terms.html'
    return render(request, template, context)


def contacts(request):
    context = get_context()
    contact_page = models.ContactPage.objects.first()
    context.update({
        'contact_page': contact_page,
    })
    if '/uz/' in request.path:
        template = 'mainapp/contacts_uz.html'
    else:
        template = 'mainapp/contacts.html'
    return render(request, template, context)


def delivery(request):
    context = get_context()
    delivery_page = models.DeliveryPage.objects.first()
    reviews = models.Reviews.objects.all()
    context.update({
        'delivery_page': delivery_page,
        'reviews': reviews,
    })
    if '/uz/' in request.path:
        template = 'mainapp/delivery_uz.html'
    else:
        template = 'mainapp/delivery.html'
    return render(request, template, context)


def services(request):
    context = get_context()
    services = models.Service.objects.all()
    context.update({
            'services': services,
        })
    if '/uz/' in request.path:
        template = 'mainapp/services_uz.html'
    else:
        template = 'mainapp/services.html'
    return render(request, template, context)


def custom_404(request, exception):
    context = get_context()
    template = 'custom_404.html'
    return render(request, template, context)

