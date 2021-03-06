# Generated by Django 3.2.8 on 2021-10-27 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0008_alter_shopping_cart_user_id'),
        ('purchase', '0004_auto_20210812_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='shopping_cart_product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='shopping_cart.shopping_cart_product'),
            preserve_default=False,
        ),
    ]
