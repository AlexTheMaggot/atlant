# Generated by Django 3.1.4 on 2021-11-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20211103_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_6',
        ),
        migrations.RemoveField(
            model_name='product',
            name='val_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='val_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='val_3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='val_4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='val_5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='val_6',
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(default=1, verbose_name='Описание на русском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(default=1, verbose_name='Описание на узбекском'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='spec_1_ru',
            field=models.CharField(default=1, max_length=200, verbose_name='Характеристика 1 (рус)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='spec_1_uz',
            field=models.CharField(default=1, max_length=200, verbose_name='Характеристика 1 (узб)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='spec_2_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 2 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_2_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 2 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_3_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 3 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_3_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 3 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_4_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 4 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_4_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 4 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_5_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 5 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_5_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 5 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_6_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 6 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='spec_6_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Характеристика 6 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_1_ru',
            field=models.CharField(default=1, max_length=200, verbose_name='Значение 1 (рус)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='val_1_uz',
            field=models.CharField(default=1, max_length=200, verbose_name='Значение 1 (узб)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='val_2_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 2 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_2_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 2 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_3_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 3 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_3_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 3 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_4_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 4 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_4_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 4 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_5_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 5 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_5_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 5 (узб)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_6_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 6 (рус)'),
        ),
        migrations.AddField(
            model_name='product',
            name='val_6_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Значение 6 (узб)'),
        ),
    ]