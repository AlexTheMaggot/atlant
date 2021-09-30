from django.shortcuts import render
from . import models
from shop.models import Category


header = models.Header.objects.first()
footer = models.Footer.objects.first()
categories = Category.objects.all()
context = {
    'header': header,
    'footer': footer,
    'categories': categories,
}


def index(request):
    main_page = models.MainPage.objects.first()
    reviews = models.Reviews.objects.all()
    partners = models.Partner.objects.all()
    worksteps = models.WorkSteps.objects.all()
    context.update({
        'main_page': main_page,
        'reviews': reviews,
        'partners': partners,
        'worksteps': worksteps,
    })
    if '/uz/' in request.path:
        template = 'mainapp/index_uz.html'
    else:
        template = 'mainapp/index.html'
    return render(request, template, context)


def about(request):
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
    services = models.Service.objects.all()
    context.update({
            'services': services,
        })
    if '/uz/' in request.path:
        template = 'mainapp/services_uz.html'
    else:
        template = 'mainapp/services.html'
    return render(request, template, context)
