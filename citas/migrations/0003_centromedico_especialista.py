# Generated by Django 5.0.8 on 2024-08-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre centro')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre especialista')),
                ('especialidad', models.CharField(max_length=200, verbose_name='Especialidad')),
            ],
        ),
    ]
