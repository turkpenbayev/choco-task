# Generated by Django 2.1.2 on 2018-11-10 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_auto_20181110_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Master'),
        ),
    ]