# Generated by Django 5.1.6 on 2025-03-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_clientes', '0004_sesiondeltest_nivel_de_dificultad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesiondeltest',
            name='limite_de_tiempo',
            field=models.IntegerField(default=1800),
        ),
    ]
