# Generated by Django 4.1.5 on 2024-06-30 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("AllBooking", "0007_rename_date_bookings_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                ("Date", models.DateField(verbose_name="日期")),
                (
                    "Day_id",
                    models.IntegerField(
                        choices=[
                            (1, "Id 1"),
                            (2, "Id 2"),
                            (3, "Id 3"),
                            (4, "Id 4"),
                            (5, "Id 5"),
                            (6, "Id 6"),
                            (7, "Id 7"),
                        ]
                    ),
                ),
                (
                    "booking_description",
                    models.CharField(max_length=100, verbose_name="項目標題"),
                ),
                (
                    "is_booking",
                    models.BooleanField(default=False, verbose_name="是否已預約"),
                ),
                (
                    "booking_slot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking",
                        to="AllBooking.timeslot",
                        verbose_name="所在時段",
                    ),
                ),
            ],
            options={
                "verbose_name": "預約內容",
                "verbose_name_plural": "預約內容",
            },
        ),
        migrations.DeleteModel(
            name="Bookings",
        ),
    ]
