# Generated by Django 4.1.7 on 2023-04-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testfield', models.CharField(max_length=200)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]