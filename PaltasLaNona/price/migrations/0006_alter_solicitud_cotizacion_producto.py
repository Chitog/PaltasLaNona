# Generated by Django 5.0.4 on 2024-05-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0005_producto_tipo_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_cotizacion',
            name='producto',
            field=models.CharField(max_length=100),
        ),
    ]