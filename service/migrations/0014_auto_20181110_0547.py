# Generated by Django 2.1.2 on 2018-11-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20181110_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.IntegerField(choices=[(1, 'Новый заказ'), (2, 'Услуга оказан'), (3, 'Отменен')], default=1, verbose_name='Тип платежа'),
        ),
    ]
