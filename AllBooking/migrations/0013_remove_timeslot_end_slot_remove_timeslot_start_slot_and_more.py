# Generated by Django 4.1.5 on 2024-07-21 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("AllBooking", "0012_alter_booking_booking_slot_alter_booking_day_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timeslot",
            name="end_slot",
        ),
        migrations.RemoveField(
            model_name="timeslot",
            name="start_slot",
        ),
        migrations.AlterField(
            model_name="booking",
            name="booking_slot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="timeslot",
                to="AllBooking.timeslot",
                verbose_name="所在時段代碼",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="day_id",
            field=models.IntegerField(
                choices=[
                    (0, "Id 0"),
                    (1, "Id 1"),
                    (2, "Id 2"),
                    (3, "Id 3"),
                    (4, "Id 4"),
                    (5, "Id 5"),
                    (6, "Id 6"),
                ],
                default=0,
                verbose_name="星期代碼",
            ),
        ),
    ]
