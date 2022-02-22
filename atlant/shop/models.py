from django.db import models


class Category(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    slug = models.SlugField(verbose_name='URL-адрес')
    top_btn_1 = models.BooleanField(verbose_name='Первая топ-категория')
    top_btn_2 = models.BooleanField(verbose_name='Вторая топ-категория')
    top_btn_3 = models.BooleanField(verbose_name='Третья топ-категория')
    top_btn_4 = models.BooleanField(verbose_name='Четвертая топ-категория')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']


class Product(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    slug = models.SlugField(verbose_name='URL-адрес')
    description_ru = models.TextField(verbose_name='Описание на русском')
    description_uz = models.TextField(verbose_name='Описание на узбекском')
    category = models.ForeignKey(Category, models.PROTECT, verbose_name='Категория', related_name='products')
    rent = models.BooleanField(verbose_name='Аренда')
    sell = models.BooleanField(verbose_name='Продажа')
    img_1 = models.ImageField(verbose_name='Основное изображение товара (960х1280)', upload_to='product_img/')
    img_2 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)', upload_to='product_img/',
                              null=True, blank=True)
    img_3 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)', upload_to='product_img/',
                              null=True, blank=True)
    img_4 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)', upload_to='product_img/',
                              null=True, blank=True)
    img_5 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)', upload_to='product_img/',
                              null=True, blank=True)
    spec_1_ru = models.CharField(verbose_name='Характеристика 1 (рус)', max_length=200)
    val_1_ru = models.CharField(verbose_name='Значение 1 (рус)', max_length=200)
    spec_2_ru = models.CharField(verbose_name='Характеристика 2 (рус)', max_length=200, null=True, blank=True)
    val_2_ru = models.CharField(verbose_name='Значение 2 (рус)', max_length=200, null=True, blank=True)
    spec_3_ru = models.CharField(verbose_name='Характеристика 3 (рус)', max_length=200, null=True, blank=True)
    val_3_ru = models.CharField(verbose_name='Значение 3 (рус)', max_length=200, null=True, blank=True)
    spec_4_ru = models.CharField(verbose_name='Характеристика 4 (рус)', max_length=200, null=True, blank=True)
    val_4_ru = models.CharField(verbose_name='Значение 4 (рус)', max_length=200, null=True, blank=True)
    spec_5_ru = models.CharField(verbose_name='Характеристика 5 (рус)', max_length=200, null=True, blank=True)
    val_5_ru = models.CharField(verbose_name='Значение 5 (рус)', max_length=200, null=True, blank=True)
    spec_6_ru = models.CharField(verbose_name='Характеристика 6 (рус)', max_length=200, null=True, blank=True)
    val_6_ru = models.CharField(verbose_name='Значение 6 (рус)', max_length=200, null=True, blank=True)
    spec_1_uz = models.CharField(verbose_name='Характеристика 1 (узб)', max_length=200)
    val_1_uz = models.CharField(verbose_name='Значение 1 (узб)', max_length=200)
    spec_2_uz = models.CharField(verbose_name='Характеристика 2 (узб)', max_length=200, null=True, blank=True)
    val_2_uz = models.CharField(verbose_name='Значение 2 (узб)', max_length=200, null=True, blank=True)
    spec_3_uz = models.CharField(verbose_name='Характеристика 3 (узб)', max_length=200, null=True, blank=True)
    val_3_uz = models.CharField(verbose_name='Значение 3 (узб)', max_length=200, null=True, blank=True)
    spec_4_uz = models.CharField(verbose_name='Характеристика 4 (узб)', max_length=200, null=True, blank=True)
    val_4_uz = models.CharField(verbose_name='Значение 4 (узб)', max_length=200, null=True, blank=True)
    spec_5_uz = models.CharField(verbose_name='Характеристика 5 (узб)', max_length=200, null=True, blank=True)
    val_5_uz = models.CharField(verbose_name='Значение 5 (узб)', max_length=200, null=True, blank=True)
    spec_6_uz = models.CharField(verbose_name='Характеристика 6 (узб)', max_length=200, null=True, blank=True)
    val_6_uz = models.CharField(verbose_name='Значение 6 (узб)', max_length=200, null=True, blank=True)
    file_1 = models.FileField(verbose_name='Файл 1', upload_to='product_files/', null=True, blank=True)
    file_1_name_ru = models.CharField(verbose_name='Название файла 1 на русском', max_length=200, null=True, blank=True)
    file_1_name_uz = models.CharField(verbose_name='Название файла 1 на узбекском', max_length=200,
                                      null=True, blank=True)
    file_2 = models.FileField(verbose_name='Файл 2', upload_to='product_files/', null=True, blank=True)
    file_2_name_ru = models.CharField(verbose_name='Название файла 2 на русском', max_length=200, null=True, blank=True)
    file_2_name_uz = models.CharField(verbose_name='Название файла 2 на узбекском', max_length=200,
                                      null=True, blank=True)
    file_3 = models.FileField(verbose_name='Файл 3', upload_to='product_files/', null=True, blank=True)
    file_3_name_ru = models.CharField(verbose_name='Название файла 3 на русском', max_length=200, null=True, blank=True)
    file_3_name_uz = models.CharField(verbose_name='Название файла 3 на узбекском', max_length=200,
                                      null=True, blank=True)
    file_4 = models.FileField(verbose_name='Файл 4', upload_to='product_files/', null=True, blank=True)
    file_4_name_ru = models.CharField(verbose_name='Название файла 4 на русском', max_length=200, null=True, blank=True)
    file_4_name_uz = models.CharField(verbose_name='Название файла 4 на узбекском', max_length=200,
                                      null=True, blank=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-id']


class RentCategory(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    slug = models.SlugField(verbose_name='URL')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Категория аренды'
        verbose_name_plural = 'Категории аренды'


class RentProduct(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    slug = models.SlugField(verbose_name='URL')
    category = models.ForeignKey(RentCategory, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='products')
    img_1 = models.ImageField(verbose_name='Основное изображение товара (960х1280)', upload_to='rent_product_img/')
    img_2 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)',
                              upload_to='rent_product_img/', null=True, blank=True)
    img_3 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)',
                              upload_to='rent_product_img/', null=True, blank=True)
    img_4 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)',
                              upload_to='rent_product_img/', null=True, blank=True)
    img_5 = models.ImageField(verbose_name='Дополнительное изображение товара (960х1280)',
                              upload_to='rent_product_img/', null=True, blank=True)
    term = models.CharField(verbose_name='Срок(в днях)', max_length=200)
    width = models.CharField(verbose_name='Ширина', max_length=200)
    height = models.CharField(verbose_name='Высота', max_length=200)
    length = models.CharField(verbose_name='Длинна', max_length=200)
    max_height = models.CharField(verbose_name='Максимальная высота', max_length=200)
    max_load = models.CharField(verbose_name='Максимальная нагрузка', max_length=200)
    quantity = models.CharField(verbose_name='Количество в комплекте', max_length=200)
    material_ru = models.CharField(verbose_name='Материал (на русском)', max_length=200)
    material_uz = models.CharField(verbose_name='Материал (на узбекском)', max_length=200)
    country_ru = models.CharField(verbose_name='Страна производителя (на русском)', max_length=200)
    country_uz = models.CharField(verbose_name='Страна производителя (на узбекском)', max_length=200)
    self_pickup = models.BooleanField(verbose_name='Возможность самовывоза')
    delivery = models.BooleanField(verbose_name='Возможность доставки')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Арендуемый товар'
        verbose_name_plural = 'Арендуемые товары'
