from django.db import models


class Category(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    slug = models.SlugField(verbose_name='URL-адрес')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=200)
    name_uz = models.CharField(verbose_name='Название на узбекском', max_length=200)
    slug = models.SlugField(verbose_name='URL-адрес')
    category = models.ForeignKey(Category, models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'