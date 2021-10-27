# Generated by Django 3.2 on 2021-05-04 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country_created_date', models.DateField(auto_now=True)),
                ('country_updated_date', models.DateField(auto_now=True)),
                ('country_created_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('country_updated_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
