# Generated by Django 3.2 on 2021-07-18 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorite', '0005_favorite_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
