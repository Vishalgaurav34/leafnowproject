# Generated by Django 3.1.3 on 2020-11-26 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
    ]
