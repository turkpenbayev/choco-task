# Generated by Django 2.1.2 on 2018-11-10 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='master',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_master', to=settings.AUTH_USER_MODEL),
        ),
    ]
