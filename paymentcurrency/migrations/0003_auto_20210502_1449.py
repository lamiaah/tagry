# Generated by Django 3.2 on 2021-05-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentcurrency', '0002_auto_20210428_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcurrency',
            name='currency_code',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='paymentcurrency',
            name='currency_name',
            field=models.CharField(default='', max_length=35, unique=True),
        ),
    ]
