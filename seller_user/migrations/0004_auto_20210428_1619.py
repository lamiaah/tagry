# Generated by Django 3.2 on 2021-04-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_user', '0003_rename_describton_seller_seller_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_address',
            field=models.CharField(default='', max_length=125),
        ),
        migrations.AddField(
            model_name='seller',
            name='website',
            field=models.CharField(blank=True, default='', max_length=225, null=True),
        ),
    ]
