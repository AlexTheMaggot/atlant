from django.db import models


class Header(models.Model):
    logo = models.ImageField(verbose_name='Логотип (303х90)', upload_to='header/img/')
    address_ru = models.CharField(verbose_name='Адрес на русском', max_length=200)
    address_uz = models.CharField(verbose_name='Адрес на на узбекском', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20)
    telegram = models.CharField(verbose_name='Telegram', max_length=200)
    instagram = models.CharField(verbose_name='Instagram', max_length=200)
    facebook = models.CharField(verbose_name='Facebook', max_length=200)
    youtube_1 = models.CharField(verbose_name='Youtube 1', max_length=200)
    youtube_2 = models.CharField(verbose_name='Youtube 2', max_length=200)

    def __str__(self):
        return self.address_ru

    class Meta:
        verbose_name = 'Шапка сайта'
        verbose_name_plural = 'Шапка сайта'


class Footer(models.Model):
    telegram = models.CharField(verbose_name='Telegram', max_length=200)
    instagram = models.CharField(verbose_name='Instagram', max_length=200)
    facebook = models.CharField(verbose_name='Facebook', max_length=200)
    youtube_1 = models.CharField(verbose_name='Youtube 1', max_length=200)
    youtube_2 = models.CharField(verbose_name='Youtube 2', max_length=200)
    worktime_ru = models.CharField(verbose_name='Режим работы на русском', max_length=200)
    worktime_uz = models.CharField(verbose_name='Режим работы на узбекском', max_length=200)
    address_ru = models.CharField(verbose_name='Адрес на русском', max_length=200)
    address_uz = models.CharField(verbose_name='Адрес на на узбекском', max_length=200)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20)

    def __str__(self):
        return self.address_ru

    class Meta:
        verbose_name = 'Подвал сайта'
        verbose_name_plural = 'Подвал сайта'


class WorkSteps(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    img = models.ImageField(verbose_name='Изображение (115х69)', upload_to='mainpage/steps/')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Этап работ'
        verbose_name_plural = 'Этапы работ'


class MainPage(models.Model):
    first_block_title_ru = models.CharField(verbose_name='Заголовок первого блока на русском', max_length=200)
    first_block_title_uz = models.CharField(verbose_name='Заголовок первого блока на узбекском', max_length=200)
    first_block_description_ru = models.TextField(verbose_name='Описание первого блока на русском')
    first_block_description_uz = models.TextField(verbose_name='Описание первого блока на узбекском')
    about_par_1_ru = models.TextField(verbose_name='О компании Первый абзац на русском')
    about_par_2_ru = models.TextField(verbose_name='О компании Второй абзац на русском')
    about_par_1_uz = models.TextField(verbose_name='О компании Первый абзац на узбекском')
    about_par_2_uz = models.TextField(verbose_name='О компании Второй абзац на узбекском')
    about_img = models.ImageField(verbose_name='О компании Изображение (464х411)', upload_to='mainpage/')
    client = models.IntegerField(verbose_name='Счетчик клиентов')
    sold = models.IntegerField(verbose_name='Счетчик проданных товаров')
    success = models.IntegerField(verbose_name='Счетчик успешных заказов')

    def __str__(self):
        return self.first_block_title_ru

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Reviews(models.Model):
    name = models.CharField(verbose_name='Имя или название компании', max_length=200)
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Partner(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    img = models.ImageField(verbose_name='Изображение (244х133)', upload_to='mainpage/partners/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class ContactPage(models.Model):
    phone_title_1_ru = models.CharField(verbose_name='Название телефона 1 на русском', max_length=200)
    phone_title_1_uz = models.CharField(verbose_name='Название телефона 1 на узбекском', max_length=200)
    phone_1 = models.CharField(verbose_name='Телефон 1', max_length=200)
    phone_title_2_ru = models.CharField(verbose_name='Название телефона 2 на русском', max_length=200, null=True, blank=True)
    phone_title_2_uz = models.CharField(verbose_name='Название телефона 2 на узбекском', max_length=200, null=True, blank=True)
    phone_2 = models.CharField(verbose_name='Телефон 2', max_length=200, null=True, blank=True)
    phone_title_3_ru = models.CharField(verbose_name='Название телефона 3 на русском', max_length=200, null=True, blank=True)
    phone_title_3_uz = models.CharField(verbose_name='Название телефона 3 на узбекском', max_length=200, null=True, blank=True)
    phone_3 = models.CharField(verbose_name='Телефон 3', max_length=200, null=True, blank=True)
    phone_title_4_ru = models.CharField(verbose_name='Название телефона 4 на русском', max_length=200, null=True, blank=True)
    phone_title_4_uz = models.CharField(verbose_name='Название телефона 4 на узбекском', max_length=200, null=True, blank=True)
    phone_4 = models.CharField(verbose_name='Телефон 4', max_length=200, null=True, blank=True)
    phone_title_5_ru = models.CharField(verbose_name='Название телефона 5 на русском', max_length=200, null=True, blank=True)
    phone_title_5_uz = models.CharField(verbose_name='Название телефона 5 на узбекском', max_length=200, null=True, blank=True)
    phone_5 = models.CharField(verbose_name='Телефон 5', max_length=200, null=True, blank=True)
    mail_title_1_ru = models.CharField(verbose_name='Название почты 1 на русском', max_length=200)
    mail_title_1_uz = models.CharField(verbose_name='Название почты 1 на узбекском', max_length=200)
    mail_1 = models.CharField(verbose_name='Почта 1', max_length=200)
    mail_title_2_ru = models.CharField(verbose_name='Название почты 2 на русском', max_length=200, null=True, blank=True)
    mail_title_2_uz = models.CharField(verbose_name='Название почты 2 на узбекском', max_length=200, null=True, blank=True)
    mail_2 = models.CharField(verbose_name='Почта 2', max_length=200, null=True, blank=True)
    mail_title_3_ru = models.CharField(verbose_name='Название почты 3 на русском', max_length=200, null=True, blank=True)
    mail_title_3_uz = models.CharField(verbose_name='Название почты 3 на узбекском', max_length=200, null=True, blank=True)
    mail_3 = models.CharField(verbose_name='Почта 3', max_length=200, null=True, blank=True)
    mail_title_4_ru = models.CharField(verbose_name='Название почты 4 на русском', max_length=200, null=True, blank=True)
    mail_title_4_uz = models.CharField(verbose_name='Название почты 4 на узбекском', max_length=200, null=True, blank=True)
    mail_4 = models.CharField(verbose_name='Почта 4', max_length=200, null=True, blank=True)
    mail_title_5_ru = models.CharField(verbose_name='Название почты 5 на русском', max_length=200, null=True, blank=True)
    mail_title_5_uz = models.CharField(verbose_name='Название почты 5 на узбекском', max_length=200, null=True, blank=True)
    mail_5 = models.CharField(verbose_name='Почта 5', max_length=200, null=True, blank=True)
    address_title_1_ru = models.CharField(verbose_name='Название адреса 1 на русском', max_length=200)
    address_title_1_uz = models.CharField(verbose_name='Название адреса 1 на узбекском', max_length=200)
    address_1_ru = models.CharField(verbose_name='Адрес 1 на русском', max_length=200)
    address_1_uz = models.CharField(verbose_name='Адрес 1 на узбекском', max_length=200)
    address_title_2_ru = models.CharField(verbose_name='Название адреса 2 на русском', max_length=200, null=True, blank=True)
    address_title_2_uz = models.CharField(verbose_name='Название адреса 2 на узбекском', max_length=200, null=True, blank=True)
    address_2_ru = models.CharField(verbose_name='Адрес 2 на русском', max_length=200, null=True, blank=True)
    address_2_uz = models.CharField(verbose_name='Адрес 2 на узбекском', max_length=200, null=True, blank=True)
    address_title_3_ru = models.CharField(verbose_name='Название адреса 3 на русском', max_length=200, null=True, blank=True)
    address_title_3_uz = models.CharField(verbose_name='Название адреса 3 на узбекском', max_length=200, null=True, blank=True)
    address_3_ru = models.CharField(verbose_name='Адрес 3 на русском', max_length=200, null=True, blank=True)
    address_3_uz = models.CharField(verbose_name='Адрес 3 на узбекском', max_length=200, null=True, blank=True)
    address_title_4_ru = models.CharField(verbose_name='Название адреса 4 на русском', max_length=200, null=True, blank=True)
    address_title_4_uz = models.CharField(verbose_name='Название адреса 4 на узбекском', max_length=200, null=True, blank=True)
    address_4_ru = models.CharField(verbose_name='Адрес 4 на русском', max_length=200, null=True, blank=True)
    address_4_uz = models.CharField(verbose_name='Адрес 4 на узбекском', max_length=200, null=True, blank=True)
    address_title_5_ru = models.CharField(verbose_name='Название адреса 5 на русском', max_length=200, null=True, blank=True)
    address_title_5_uz = models.CharField(verbose_name='Название адреса 5 на узбекском', max_length=200, null=True, blank=True)
    address_5_ru = models.CharField(verbose_name='Адрес 5 на русском', max_length=200, null=True, blank=True)
    address_5_uz = models.CharField(verbose_name='Адрес 5 на узбекском', max_length=200, null=True, blank=True)
    callback_text_ru = models.TextField(verbose_name='Текст обратной связи на русском')
    callback_text_uz = models.TextField(verbose_name='Текст обратной связи на узбекском')

    def __str__(self):
        return self.phone_1

    class Meta:
        verbose_name = 'Страница "Контакты"'
        verbose_name_plural = 'Страница "Контакты"'


class RentTermPage(models.Model):
    benefits_ru = models.TextField(verbose_name='Преимущества аренды на русском')
    benefits_uz = models.TextField(verbose_name='Преимущества аренды на узбекском')
    suggestions_ru = models.TextField(verbose_name='Наши предложения на русском')
    suggestions_uz = models.TextField(verbose_name='Наши предложения на узбекском')

    def __str__(self):
        return self.benefits_ru

    class Meta:
        verbose_name = 'Страница "Условия аренды"'
        verbose_name_plural = 'Страница "Условия аренды"'


class DeliveryPage(models.Model):
    text_ru = models.TextField(verbose_name='Текст страницы на русском')
    text_uz = models.TextField(verbose_name='Текст страницы на узбекском')

    def __str__(self):
        return self.text_ru

    class Meta:
        verbose_name = 'Страница "Доставка"'
        verbose_name_plural = 'Страница "Доставка"'


class Service(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    desc_1_ru = models.TextField(verbose_name='Краткое описание на русском')
    desc_1_uz = models.TextField(verbose_name='Краткое описание на узбекском')
    object_name_1_ru = models.CharField(verbose_name='Название первого объекта на русском', max_length=200)
    object_name_1_uz = models.CharField(verbose_name='Название первого объекта на узбекском', max_length=200)
    object_desc_1_ru = models.CharField(verbose_name='Описание первого обекта на русском', max_length=200)
    object_desc_1_uz = models.CharField(verbose_name='Описание первого обекта на узбекском', max_length=200)
    object_img_1 = models.ImageField(verbose_name='Изображение первого объекта (232х232)', upload_to='services/')
    object_name_2_ru = models.CharField(verbose_name='Название второго объекта на русском', max_length=200)
    object_name_2_uz = models.CharField(verbose_name='Название второго объекта на узбекском', max_length=200)
    object_desc_2_ru = models.CharField(verbose_name='Описание второго обекта на русском', max_length=200)
    object_desc_2_uz = models.CharField(verbose_name='Описание второго обекта на узбекском', max_length=200)
    object_img_2 = models.ImageField(verbose_name='Изображение второго объекта (232х232)', upload_to='services/')
    object_name_3_ru = models.CharField(verbose_name='Название третьего объекта на русском', max_length=200)
    object_name_3_uz = models.CharField(verbose_name='Название третьего объекта на узбекском', max_length=200)
    object_desc_3_ru = models.CharField(verbose_name='Описание третьего обекта на русском', max_length=200)
    object_desc_3_uz = models.CharField(verbose_name='Описание третьего обекта на узбекском', max_length=200)
    object_img_3 = models.ImageField(verbose_name='Изображение третьего объекта (232х232)', upload_to='services/')
    object_name_4_ru = models.CharField(verbose_name='Название четвертого объекта на русском', max_length=200)
    object_name_4_uz = models.CharField(verbose_name='Название четвертого объекта на узбекском', max_length=200)
    object_desc_4_ru = models.CharField(verbose_name='Описание четвертого обекта на русском', max_length=200)
    object_desc_4_uz = models.CharField(verbose_name='Описание четвертого обекта на узбекском', max_length=200)
    object_img_4 = models.ImageField(verbose_name='Изображение четвертого объекта (232х232)', upload_to='services/')
    desc_2_ru = models.TextField(verbose_name='Полное описание на русском')
    desc_2_uz = models.TextField(verbose_name='Полное описание на узбекском')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class AboutPage(models.Model):
    text_1_ru = models.TextField(verbose_name='Краткое описание на русском')
    text_1_uz = models.TextField(verbose_name='Краткое описание на узбекском')
    text_2_ru = models.TextField(verbose_name='Полное описание на русском')
    text_2_uz = models.TextField(verbose_name='Полное описание на узбекском')
    year = models.IntegerField(verbose_name='Лет на рынке')
    order = models.IntegerField(verbose_name='Количество заказов')
    delivery = models.IntegerField(verbose_name='Количество доставок')
    repeated = models.IntegerField(verbose_name='Процент повторных обращений')

    def __str__(self):
        return self.text_1_ru

    class Meta:
        verbose_name = 'Страница "О компании"'
        verbose_name_plural = 'Страница "О компании"'