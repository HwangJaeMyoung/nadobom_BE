# Generated by Django 4.1.7 on 2023-05-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='altitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='report',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]