# Generated by Django 5.0.2 on 2024-03-10 11:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0002_alter_project_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="link",
            new_name="url",
        ),
    ]
