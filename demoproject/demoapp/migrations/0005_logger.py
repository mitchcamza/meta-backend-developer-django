# Generated by Django 4.1.5 on 2023-01-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0004_person_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="Logger",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("time_log", models.TimeField(help_text="Enter the exact time!")),
            ],
        ),
    ]
