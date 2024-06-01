# Generated by Django 4.2.11 on 2024-06-01 16:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "category_label",
                    models.TextField(primary_key=True, serialize=False, unique=True),
                ),
                ("category_id", models.TextField()),
                ("category_code", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Content",
            fields=[
                ("content_id", models.AutoField(primary_key=True, serialize=False)),
                ("content_source_id", models.TextField()),
                ("content_headline", models.TextField(unique=True)),
                ("content_source", models.TextField()),
                ("content_url", models.TextField()),
                ("content_category", models.TextField()),
                ("content_text", models.TextField()),
                ("content_image", models.TextField()),
                ("content_date", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Option",
            fields=[
                ("option_id", models.AutoField(primary_key=True, serialize=False)),
                ("snippet_id", models.IntegerField()),
                (
                    "option_default",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=50),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                (
                    "option_added",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=20),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Snippet",
            fields=[
                ("snippet_id", models.AutoField(primary_key=True, serialize=False)),
                ("thread_id", models.IntegerField()),
                ("snippet_text", models.TextField()),
                ("time_to_consume", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                ("source_id", models.AutoField(primary_key=True, serialize=False)),
                ("source_url", models.URLField(default="")),
                ("source_trust_rating", models.IntegerField(default=0)),
                ("source_name", models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Thread",
            fields=[
                ("thread_id", models.AutoField(primary_key=True, serialize=False)),
                ("content_id", models.IntegerField()),
                ("content_title", models.TextField()),
                ("type", models.TextField()),
                ("sentiment_valence", models.TextField()),
                ("sentiment_arousal", models.TextField()),
                ("style", models.TextField()),
                ("tone", models.TextField()),
            ],
        ),
    ]
