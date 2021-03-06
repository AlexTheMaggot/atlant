# Generated by Django 3.1.4 on 2022-02-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20211108_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='meta_description',
            field=models.TextField(default=123, verbose_name='Meta Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainpage',
            name='meta_keywords',
            field=models.CharField(default=123, max_length=200, verbose_name='Meta Keywords'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainpage',
            name='meta_title',
            field=models.CharField(default=123, max_length=200, verbose_name='Meta Title'),
            preserve_default=False,
        ),
    ]
