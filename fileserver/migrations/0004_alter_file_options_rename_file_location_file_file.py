# Generated by Django 4.2.7 on 2024-01-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fileserver", "0003_delete_client"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="file",
            options={"permissions": []},
        ),
        migrations.RenameField(
            model_name="file",
            old_name="file_location",
            new_name="file",
        ),
    ]