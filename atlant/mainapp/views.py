from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail

from . import models
from shop.models import Category, Product, RentCategory, RentProduct


MAIL_TO = 'atlantgroups1@gmail.com'


def get_context():
    header = models.Header.objects.first()
    footer = models.Footer.objects.first()
    categories = Category.objects.all()
    rent_categories = RentCategory.objects.all()
    reviews = models.Reviews.objects.all()
    context = {
        'header': header,
        'footer': footer,
        'categories': categories,
        'rent_categories': rent_categories,
        'reviews': reviews,
    }
    return context


def index(request):
    context = get_context()
    main_page = models.MainPage.objects.first()
    partners = models.Partner.objects.all()
    worksteps = models.WorkSteps.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(1)
    context.update({
        'main_page': main_page,
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
    about_page = models.AboutPage.objects.first()
    context.update({
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
    context.update({
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
    context.update({
        'delivery_page': delivery_page,
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


def callback_send(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}'.format(request.POST['name'], request.POST['phone'])
        if request.POST['quantity']:
            message += '\nКоличество: ' + str(request.POST['quantity'])
        if request.POST['time']:
            message += '\nСрок: ' + str(request.POST['time'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def another_callback_send(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}'.format(request.POST['name'], request.POST['phone'])
        if request.POST['time_to_call']:
            message += '\nУдобное время для звонка: ' + str(request.POST['time_to_call'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def one_more_callback_send(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}'.format(request.POST['name'], request.POST['phone'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def rent_order(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}\nПродукт: {2}'.format(
            request.POST['name'],
            request.POST['phone'],
            request.POST['rent_product']
        )
        if request.POST['quantity']:
            message += '\n\nКоличество: ' + str(request.POST['quantity'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def not_found_send(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}'.format(
            request.POST['name'],
            request.POST['phone'],
        )
        if request.POST['time']:
            message += '\n\nУдобное время для звонка: ' + str(request.POST['time'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def product_order(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}'.format(
            request.POST['name'],
            request.POST['phone'],
        )
        if request.POST['type'] == 'buy':
            message += '\n\nТип: Покупка'
        elif request.POST['type'] == 'ask':
            message += '\n\nТип: Узнать цену и условия'
        else:
            message += '\n\nТип: Аренда'
            if request.POST['time']:
                message += '\n\nСрок: ' + str(request.POST['time'])
        if request.POST['quantity']:
            message += '\n\nКоличество: ' + str(request.POST['quantity'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def service_order(request):
    if request.method == "POST":
        subject = 'Новая заявка!'
        message = 'Имя: {0}\nТелефон: {1}'.format(request.POST['name'], request.POST['phone'])
        if request.POST['text']:
            message += '\n\nСообщение: ' + str(request.POST['text'])
        send_mail(subject, message, 'no-reply@atlant-group.uz', [MAIL_TO])
        if request.POST['lang'] == 'uz':
            return redirect('mainapp_uz:thank_you')
        else:
            return redirect('mainapp:thank_you')
    else:
        return redirect('mainapp:index')


def thank_you(request):
    context = get_context()
    if '/uz/' in request.path:
        template = 'mainapp/thank_you_uz.html'
    else:
        template = 'mainapp/thank_you.html'
    return render(request, template, context)
