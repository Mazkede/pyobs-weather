# Generated by Django 2.2.4 on 2019-08-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_station_plot'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='color',
            field=models.CharField(default='black', max_length=10, verbose_name='Plot color'),
        ),
    ]
