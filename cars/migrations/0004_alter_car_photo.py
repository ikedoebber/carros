# Generated by Django 5.0.7 on 2024-08-03 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0003_car_photo_car_plate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="cars//"),
        ),
    ]
