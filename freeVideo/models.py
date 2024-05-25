from django.db import models

class FreeVideos(models.Model):
      video_img=models.URLField(max_length=300,verbose_name='影片圖片連結'
      , default='https://www.google.com.tw/url?sa=i&url=https%3A%2F%2Fwww.soundofhope.org%2Fpost%2F278421%3Flang%3Db5&psig=AOvVaw0_XGf_qSapc66CW8u2_xMR&ust=1716697830144000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLj_-4D8p4YDFQAAAAAdAAAAABAP' )
      video_title=models.CharField(max_length=30,verbose_name='影片標題')
      video_description=models.TextField(max_length=300,verbose_name='影片敘述')
      video_link=models.URLField(max_length=300,verbose_name='影片連結')
      pub_date=models.DateTimeField(auto_now_add=True,verbose_name='影片發布日期')

      class Meta:
            ordering=('-pub_date',)

      def __str__(self):
            return self.video_title