from django.db import models
from datetime import datetime, date
import calendar

weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 不同時段的部分
class TimeSlot(models.Model):
    start_slot = models.TimeField(verbose_name='開始時點')
    end_slot = models.TimeField(verbose_name='結束時點')

    def slot_difference(self):
        start_daytime = datetime.combine(datetime.today(), self.start_slot)
        end_daytime = datetime.combine(datetime.today(), self.end_slot)
        difference = end_daytime - start_daytime
        return difference

    slot_description = models.CharField(max_length=100, verbose_name='時段描述')

    class Meta:
        verbose_name = '預約時段'
        verbose_name_plural = '預約時段'

    def __str__(self):
        Difference = self.slot_difference()
        return f"{self.slot_description}- ({Difference})"
    
    
class MyChoices(models.IntegerChoices):
    ID_1 = 1
    ID_2 = 2
    ID_3 = 3
    ID_4= 4
    ID_5= 5
    ID_6 = 6
    ID_7 = 7

# 不同預約項目 ( 包含日期，預約標題 ，是否可預約的判斷等)
d = date.today()
x_day = calendar.day_name[d.weekday()]

class Bookings(models.Model):
    Date = models.DateField(verbose_name='日期')
    booking_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='booking', verbose_name='所在時段')

    # 定義 Day_id 的初始值
    if x_day == 'Monday':
        initial_day_id = MyChoices.ID_1
    elif x_day == 'Tuesday':
        initial_day_id = MyChoices.ID_2
    elif x_day == 'Wednesday':
        initial_day_id = MyChoices.ID_3
    elif x_day == 'Thursday':
        initial_day_id = MyChoices.ID_4
    elif x_day == 'Friday':
        initial_day_id = MyChoices.ID_5
    elif x_day == 'Saturday':
        initial_day_id = MyChoices.ID_6
    elif x_day == 'Sunday':
        initial_day_id = MyChoices.ID_7

    Day_id = models.IntegerField(choices=MyChoices.choices)
    
    booking_description = models.CharField(max_length=100, verbose_name='項目標題')
    is_booking = models.BooleanField(default=False, verbose_name='是否已預約')

    class Meta:
        verbose_name = '預約內容'
        verbose_name_plural = '預約內容'
    
    def __str__(self):
        return f"{self.Date}-{self.booking_slot}-{self.Day_id}:{self.booking_description}-{self.is_booking}"
