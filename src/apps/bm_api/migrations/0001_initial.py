# Generated by Django 5.2 on 2025-04-08 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DirectorName",
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
                ("full_name", models.CharField(max_length=120)),
            ],
            options={
                "verbose_name": "Director Name",
                "verbose_name_plural": "Directors Names",
            },
        ),
    ]
