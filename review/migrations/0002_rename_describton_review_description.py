# Generated by Django 3.2 on 2021-04-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='describton',
            new_name='description',
        ),
    ]
