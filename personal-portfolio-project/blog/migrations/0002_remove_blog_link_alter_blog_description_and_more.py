# Generated by Django 5.0.2 on 2024-03-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="link",
        ),
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]