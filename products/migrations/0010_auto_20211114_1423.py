# Generated by Django 3.2 on 2021-11-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210912_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='product_pic/')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='products.products')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
