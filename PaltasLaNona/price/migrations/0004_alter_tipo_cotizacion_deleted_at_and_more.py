# Generated by Django 5.0.4 on 2024-05-16 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_alter_tipo_cotizacion_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_cotizacion',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tipo_entrega',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
