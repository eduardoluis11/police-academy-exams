# Generated by Django 5.1.6 on 2025-03-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_administradores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntadeltest',
            name='nombre_del_test',
        ),
        migrations.AddField(
            model_name='preguntadeltest',
            name='nombre_del_test',
            field=models.ManyToManyField(to='tests_administradores.test'),
        ),
    ]
