from django.db import models

class FreeVideos(models.Model):
      video_title=models.CharField(max_length=30,verbose_name='影片標題')
      video_description=models.TextField(max_length=300,verbose_name='影片敘述')
      video_link=models.URLField(max_length=300,verbose_name='影片連結')
      pub_date=models.DateTimeField(auto_now_add=True,verbose_name='影片發布日期')

      class Meta:
            ordering=('-pub_date',)

      def __str__(self):
            return self.video_title