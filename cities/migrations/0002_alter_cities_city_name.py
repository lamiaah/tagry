# Generated by Django 3.2 on 2021-05-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='city_name',
            field=models.CharField(default='', max_length=75, unique=True),
        ),
    ]
