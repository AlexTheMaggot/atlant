# Generated by Django 3.1.4 on 2021-11-08 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rentcategory_rentproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentproduct',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.rentcategory', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]