# Generated by Django 4.2.7 on 2024-01-06 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fileserver", "0005_file_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(
                upload_to="",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["txt", "pptx", "xlsx", "docx"]
                    )
                ],
            ),
        ),
    ]