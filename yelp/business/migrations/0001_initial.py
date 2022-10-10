# Generated by Django 4.1.2 on 2022-10-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
            fields=[
                (
                    "business_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("postal_code", models.CharField(max_length=10)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("stars", models.FloatField()),
                ("review_count", models.PositiveIntegerField(default=0)),
                ("is_open", models.PositiveIntegerField(default=0)),
                ("attributes", models.JSONField(default={})),
                ("categories", models.TextField(blank=True, null=True)),
                ("hours", models.JSONField(default={})),
            ],
        ),
    ]
