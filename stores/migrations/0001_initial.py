# Generated by Django 3.2 on 2021-11-18 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0002_alter_cities_city_name'),
        ('area', '0001_initial'),
        ('countries', '0005_alter_countries_code'),
        ('seller_user', '0014_seller_area_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerStores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(default='', max_length=75)),
                ('store_address', models.CharField(default='', max_length=225)),
                ('is_archived', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='seller_user.seller')),
                ('store_area', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='area.area')),
                ('store_city', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cities.cities')),
                ('store_country', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='countries.countries')),
            ],
        ),
    ]
