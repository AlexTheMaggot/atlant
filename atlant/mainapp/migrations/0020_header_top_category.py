# Generated by Django 3.1.4 on 2021-10-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
        ('mainapp', '0019_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='top_category',
            field=models.ManyToManyField(to='shop.Category', verbose_name='Топ категорий'),
        ),
    ]