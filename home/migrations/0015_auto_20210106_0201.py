# Generated by Django 3.1.3 on 2021-01-05 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210106_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='corder',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='corder',
            name='drop_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 6, 2, 1, 48, 325379)),
        ),
    ]
