# Generated by Django 4.2.7 on 2024-01-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientModel",
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
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="FileModel",
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
                ("file_name", models.CharField(max_length=225)),
                ("file_location", models.FileField(upload_to="")),
            ],
        ),
    ]