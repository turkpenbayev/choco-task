# Generated by Django 2.1.2 on 2018-11-10 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20181109_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастеры',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('detail', models.TextField(max_length=512, verbose_name='Подробне')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.AddField(
            model_name='master',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service', verbose_name='Услуга'),
        ),
        migrations.AddField(
            model_name='master',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
