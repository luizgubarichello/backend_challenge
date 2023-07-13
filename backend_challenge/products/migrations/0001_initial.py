# Generated by Django 4.2.2 on 2023-07-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "code",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("barcode", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("imported", "Imported")],
                        max_length=10,
                    ),
                ),
                ("imported_t", models.DateTimeField()),
                ("url", models.URLField()),
                ("product_name", models.CharField(max_length=200)),
                ("quantity", models.CharField(max_length=50)),
                ("categories", models.CharField(max_length=200)),
                ("packaging", models.CharField(max_length=200)),
                ("brands", models.CharField(max_length=200)),
                ("image_url", models.URLField()),
            ],
        ),
    ]
