# Generated by Django 4.2.2 on 2023-07-31 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mentorship", "0004_change_group_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseImage",
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
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]
