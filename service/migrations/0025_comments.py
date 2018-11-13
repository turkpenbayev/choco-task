# Generated by Django 2.1.2 on 2018-11-11 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0024_auto_20181110_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Пользователь')),
                ('content', models.TextField(max_length=200)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Master')),
            ],
        ),
    ]