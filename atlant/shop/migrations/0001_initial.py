# Generated by Django 3.1.4 on 2021-09-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=200, verbose_name='Название на русском')),
                ('name_uz', models.CharField(max_length=200, verbose_name='Название на узбекском')),
                ('slug', models.SlugField(verbose_name='URL-адрес')),
            ],
            options={
                'verbose_name': 'Ктаегория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
