# Generated by Django 2.1.2 on 2018-11-10 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20181110_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='master',
            field=models.ManyToManyField(to='service.Master', verbose_name='Мастер'),
        ),
    ]
