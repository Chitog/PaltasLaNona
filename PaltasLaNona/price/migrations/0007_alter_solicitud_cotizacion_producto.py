# Generated by Django 5.0.4 on 2024-05-22 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0006_alter_solicitud_cotizacion_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_cotizacion',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price.producto'),
        ),
    ]