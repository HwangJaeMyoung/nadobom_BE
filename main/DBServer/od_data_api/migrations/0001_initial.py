# Generated by Django 4.1 on 2023-03-23 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("image_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="od_data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.FileField(upload_to="od_data/labels/")),
                (
                    "image_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="image_api.image",
                    ),
                ),
            ],
        ),
    ]