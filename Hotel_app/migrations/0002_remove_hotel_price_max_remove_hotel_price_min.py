# Generated by Django 5.0.2 on 2024-02-13 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Hotel_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hotel",
            name="price_max",
        ),
        migrations.RemoveField(
            model_name="hotel",
            name="price_min",
        ),
    ]