# Generated by Django 3.2 on 2021-05-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20210502_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='category_title',
            field=models.CharField(default='', max_length=75, unique=True),
        ),
    ]
