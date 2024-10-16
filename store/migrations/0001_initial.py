# Generated by Django 5.0.8 on 2024-10-16 17:59

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="Enter Category Name",
                        max_length=250,
                        verbose_name="Category Name",
                    ),
                ),
                ("slug", models.SlugField(max_length=250, unique=True)),
            ],
            options={
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=250)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default.png", upload_to="images/%Y/%m/%d/"
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=4)),
                (
                    "discount",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=4
                    ),
                ),
                ("available", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.category"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "products",
                "ordering": ("title",),
            },
        ),
    ]
