# Generated by Django 4.2 on 2023-05-01 10:54

from django.db import migrations, models
import django.db.models.deletion


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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                ("categories", models.ManyToManyField(to="product.category")),
            ],
        ),
        migrations.CreateModel(
            name="Topping",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PizzaImg",
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
                ("image", models.CharField(max_length=9999)),
                (
                    "pizza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.pizza"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pizza",
            name="toppings",
            field=models.ManyToManyField(to="product.topping"),
        ),
        migrations.CreateModel(
            name="OfferImg",
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
                ("image", models.CharField(max_length=9999)),
                (
                    "offer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.offer"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="offer",
            name="pizzas",
            field=models.ManyToManyField(to="product.pizza"),
        ),
    ]
