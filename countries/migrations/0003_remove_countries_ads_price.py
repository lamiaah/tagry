# Generated by Django 3.2 on 2021-05-02 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_countries_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='ads_price',
        ),
    ]
