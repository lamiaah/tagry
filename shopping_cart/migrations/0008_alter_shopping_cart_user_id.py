# Generated by Django 3.2 on 2021-09-24 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_cart', '0007_alter_shopping_cart_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping_cart',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
