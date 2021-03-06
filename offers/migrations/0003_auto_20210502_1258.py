# Generated by Django 3.2 on 2021-05-02 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offers', '0002_auto_20210428_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='created_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='users.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='updated_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='users.customuser'),
            preserve_default=False,
        ),
    ]
