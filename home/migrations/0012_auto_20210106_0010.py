# Generated by Django 3.1.3 on 2021-01-05 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210105_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corder',
            name='drop_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 6, 0, 10, 28, 590740)),
        ),
        migrations.AlterField(
            model_name='corder',
            name='total',
            field=models.IntegerField(default=2),
        ),
    ]
