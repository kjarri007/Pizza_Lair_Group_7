# Generated by Django 4.2 on 2023-05-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="price",
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name="pizza",
            name="price",
            field=models.IntegerField(default=1000),
        ),
    ]
