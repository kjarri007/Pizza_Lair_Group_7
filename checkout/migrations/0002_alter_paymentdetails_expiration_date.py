# Generated by Django 4.2 on 2023-05-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentdetails",
            name="expiration_date",
            field=models.CharField(max_length=5),
        ),
    ]
