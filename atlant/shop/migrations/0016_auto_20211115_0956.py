# Generated by Django 3.1.4 on 2021-11-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20211111_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentproduct',
            name='height',
            field=models.CharField(max_length=200, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='rentproduct',
            name='length',
            field=models.CharField(max_length=200, verbose_name='Длинна'),
        ),
        migrations.AlterField(
            model_name='rentproduct',
            name='max_height',
            field=models.CharField(max_length=200, verbose_name='Максимальная высота'),
        ),
        migrations.AlterField(
            model_name='rentproduct',
            name='max_load',
            field=models.CharField(max_length=200, verbose_name='Максимальная нагрузка'),
        ),
        migrations.AlterField(
            model_name='rentproduct',
            name='quantity',
            field=models.CharField(max_length=200, verbose_name='Количество в комплекте'),
        ),
        migrations.AlterField(
            model_name='rentproduct',
            name='term',
            field=models.CharField(max_length=200, verbose_name='Срок(в днях)'),
        ),
        migrations.AlterField(
            model_name='rentproduct',
            name='width',
            field=models.CharField(max_length=200, verbose_name='Ширина'),
        ),
    ]