# Generated by Django 2.1.4 on 2019-01-17 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20190117_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='finish_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
