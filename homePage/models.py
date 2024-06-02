from django.db import models

class BookingProcess(models.Model):
      porcess_title=models.CharField(max_length=50,blank=True,verbose_name='預約標題')
      process_content=models.TextField(max_length=800,blank=True,verbose_name='預約內容')
      process_icon=models.URLField(blank=True,verbose_name='預約圖示')
      class Meta:
            verbose_name = '預約流程'
            verbose_name_plural = '預約流程'

      def __str__(self):
            return self.porcess_title

class ServiceItems(models.Model):
      service_title=models.CharField(max_length=50,blank=True,verbose_name='服務標題')
      service_content=models.TextField(max_length=800,blank=True,verbose_name='預約內容')
      class Meta:
            verbose_name = '服務項目'
            verbose_name_plural = '服務項目'

      def __str__(self):
            return self.service_title

