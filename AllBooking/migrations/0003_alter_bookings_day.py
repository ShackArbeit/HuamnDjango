# Generated by Django 5.0.6 on 2024-06-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AllBooking", "0002_alter_bookings_options_alter_timeslot_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookings",
            name="Day",
            field=models.CharField(max_length=50, verbose_name="星期幾"),
        ),
    ]
