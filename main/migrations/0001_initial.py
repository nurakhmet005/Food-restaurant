# Generated by Django 4.1.3 on 2023-02-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('phone', models.CharField(max_length=128, verbose_name='Номер телефона')),
                ('guests', models.IntegerField(verbose_name='Гостей')),
                ('time', models.DateTimeField( verbose_name='Время')),
            ],
        ),
    ]
