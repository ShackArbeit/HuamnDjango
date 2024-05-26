from django.db import models

class LayoutWhat(models.Model):
      title=models.CharField(max_length=255,verbose_name='小節標題')
      content=models.TextField(max_length=800,verbose_name='小節內容')
      content_url=models.CharField(max_length=255,verbose_name='內容連結',
      blank=True)
      img_url=models.URLField(max_length=800,verbose_name='圖片連結',blank=True) 

      def save(self,*args,**kwargs):
            if not self.content_url:
                  self.content_url =self.title
            super().save(*args, **kwargs)
      def __str__(self):
            return self.title