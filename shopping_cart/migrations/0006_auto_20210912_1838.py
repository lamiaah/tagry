# Generated by Django 3.2 on 2021-09-12 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0005_shopping_cart_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='products_id',
        ),
        migrations.RemoveField(
            model_name='shopping_cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='shopping_cart_product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shopping_cart_product',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='shopping_cart_product',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='shopping_cart_product',
            name='updated_user',
        ),
    ]
