# Generated by Django 2.1.2 on 2018-11-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20181109_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'Пользватель'), (2, 'Мастер'), (3, 'Партнер')], default=1, verbose_name='type'),
        ),
    ]
