# Generated by Django 4.0.4 on 2022-06-02 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nynet', '0004_rename_value_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.12, max_digits=9, verbose_name='Iva'),
        ),
    ]