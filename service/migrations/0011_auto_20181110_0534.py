# Generated by Django 2.1.2 on 2018-11-10 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_auto_20181110_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Salon', verbose_name='Салон'),
        ),
    ]
