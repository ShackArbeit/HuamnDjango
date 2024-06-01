from django.db import models

class aboutJeorme(models.Model):
      about_title=models.CharField(max_length=30,verbose_name='關於標題')
      about_year=models.IntegerField(verbose_name='關於年分',default=2013)
      about_content=models.TextField(max_length=800,verbose_name='關於內容')
