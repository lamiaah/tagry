# Generated by Django 3.2 on 2021-08-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_user', '0009_auto_20210510_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
    ]
