# Generated by Django 2.1.4 on 2019-01-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='finish_date',
            field=models.DateTimeField(null=True),
        ),
    ]
