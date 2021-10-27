# Generated by Django 3.2 on 2021-05-02 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_rename_product_describton_products_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='updated_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='users.customuser'),
            preserve_default=False,
        ),
    ]
