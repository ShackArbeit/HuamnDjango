from django.db import models
from datetime import datetime

class DayChoices(models.IntegerChoices):
    ID_0 = 0
    ID_1 = 1
    ID_2 = 2
    ID_3 = 3
    ID_4 = 4
    ID_5 = 5
    ID_6 = 6

class SlotChoices(models.IntegerChoices):
    ID_1 = 1
    ID_2 = 2
    ID_3 = 3
    ID_4 = 4

class TimeSlot(models.Model):
    start_slot = models.TimeField(verbose_name='開始時點')
    end_slot = models.TimeField(verbose_name='結束時點')
    slot_description = models.CharField(max_length=100, verbose_name='時段描述')
    slot_id = models.IntegerField(choices=SlotChoices.choices, default=1, verbose_name='時段代碼')

    def slot_difference(self):
        start_daytime = datetime.combine(datetime.today(), self.start_slot)
        end_daytime = datetime.combine(datetime.today(), self.end_slot)
        difference = end_daytime - start_daytime
        return difference

    class Meta:
        verbose_name = '預約時段'
        verbose_name_plural = '預約時段'

    def __str__(self):
        Difference = self.slot_difference()
        return f"(時段代碼:{self.slot_id})-{self.slot_description}-(共 {Difference} 小時)"

class Booking(models.Model):
    date = models.DateField(verbose_name='日期')
    booking_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='booking', verbose_name='所在時段')
    day_id = models.IntegerField(choices=DayChoices.choices,default=0)
    booking_description = models.CharField(max_length=100, verbose_name='項目標題')
    is_booking = models.BooleanField(default=False, verbose_name='是否已預約')

    class Meta:
        verbose_name = '預約內容'
        verbose_name_plural = '預約內容'

    def __str__(self):
        return f"{self.date}-{self.booking_slot}-{self.day_id}:{self.booking_description}-{self.is_booking}"
