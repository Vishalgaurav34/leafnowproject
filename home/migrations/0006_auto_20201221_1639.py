# Generated by Django 3.1.3 on 2020-12-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_corder'),
    ]

    operations = [
        migrations.AddField(
            model_name='corder',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='corder',
            name='carname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='corder',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='corder',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='corder',
            name='zip_code',
            field=models.CharField(default='', max_length=100),
        ),
    ]
