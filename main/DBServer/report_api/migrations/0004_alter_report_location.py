# Generated by Django 4.1.7 on 2023-05-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_api', '0003_rename_altitude_report_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
