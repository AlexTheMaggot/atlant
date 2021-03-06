# Generated by Django 3.1.4 on 2021-11-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='top_btn_1',
            field=models.BooleanField(default=1, verbose_name='Первая топ-категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='top_btn_2',
            field=models.BooleanField(default=1, verbose_name='Вторая топ-категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='top_btn_3',
            field=models.BooleanField(default=1, verbose_name='Третья топ-категория'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='top_btn_4',
            field=models.BooleanField(default=1, verbose_name='Четвертая топ-категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category', verbose_name='Категория'),
        ),
    ]
