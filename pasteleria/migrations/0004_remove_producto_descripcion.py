# Generated by Django 3.2.3 on 2021-07-02 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0003_dato_contraseña'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
    ]
