# Generated by Django 4.1.7 on 2023-04-06 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0003_image_image_url_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
    ]
