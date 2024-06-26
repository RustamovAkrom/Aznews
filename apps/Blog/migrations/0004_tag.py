# Generated by Django 5.0.3 on 2024-04-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0003_post_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=60)),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "Tags",
            },
        ),
    ]
