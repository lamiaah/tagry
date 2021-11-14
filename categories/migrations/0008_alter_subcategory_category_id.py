# Generated by Django 3.2 on 2021-11-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='categories.categories'),
        ),
    ]
