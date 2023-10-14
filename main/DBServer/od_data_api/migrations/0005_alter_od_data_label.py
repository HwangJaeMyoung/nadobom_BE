# Generated by Django 4.1.7 on 2023-07-25 06:35

from django.db import migrations, models
import image_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('od_data_api', '0004_alter_od_data_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='od_data',
            name='label',
            field=models.FileField(storage=image_api.models.S3MediaStorage(), upload_to='od_data/labels/'),
        ),
    ]
