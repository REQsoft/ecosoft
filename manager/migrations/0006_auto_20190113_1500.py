# Generated by Django 2.1.4 on 2019-01-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20190113_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='state',
            field=models.CharField(choices=[('1', 'Pendiente'), ('2', 'En proceso'), ('3', 'Terminado')], default='1', max_length=20),
        ),
    ]