# Generated by Django 5.0.8 on 2024-08-20 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carro_delete_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='car_MARCA',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='carro',
            old_name='car_ANO_FABRICACAO',
            new_name='factory_year',
        ),
        migrations.RenameField(
            model_name='carro',
            old_name='car_ID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='carro',
            old_name='car_MODELO',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='carro',
            old_name='car_ANO_MODELO',
            new_name='model_year',
        ),
        migrations.RenameField(
            model_name='carro',
            old_name='car_VALOR',
            new_name='value',
        ),
    ]
