from django.db import models

class FreeVideos(models.Model):
      video_title=models.CharField(max_length=30)
      video_description=models.TextField(max_length=300)
      video_link=models.URLField(max_length=300)
      pub_date=models.DateTimeField(auto_now_add=True)

      class Meta:
            ordering=('-pub_date',)

      def __str__(self):
            return self.video_title