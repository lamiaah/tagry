# Generated by Django 3.2 on 2021-06-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0004_remove_favorite_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='added_at',
            field=models.DateField(auto_now=True),
        ),
    ]
