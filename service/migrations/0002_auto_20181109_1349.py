# Generated by Django 2.1.2 on 2018-11-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'Пользватель'), (2, 'Мастер'), (3, 'Партнер')], verbose_name='type'),
        ),
    ]
