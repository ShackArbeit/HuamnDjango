from django.db import models

class LayoutWhat(models.Model):
      title=models.CharField(max_length=255,verbose_name='小節標題')
      content=models.TextField(max_length=800,verbose_name='小節內容')  
      img_url=models.URLField(max_length=800,verbose_name='圖片連結',blank=True) 
     
      class Meta:
            verbose_name = '簡介人類圖首頁 (各分頁的索引值)'
            verbose_name_plural = '簡介人類圖首頁 (各分頁的索引值)'

      def __str__(self):
            return self.title


class HumanContentCommon(models.Model):
      layout_key = models.ForeignKey(LayoutWhat, on_delete=models.CASCADE,
      default='人類圖是你的人生使用說明書')
      title=models.CharField(max_length=300,verbose_name='內容標題')
      content=models.TextField(verbose_name='標題內容')
      imgs_url=models.URLField(blank=True,verbose_name='內容圖片')
      class Meta:
            abstract = True
      def __str__(self):
            return self.title
# 人類圖是你的使用說明書部分
class YourBooks(HumanContentCommon):
      class Meta:
        verbose_name = '人類圖是你的人生使用說明書部分(索引值1)'
        verbose_name_plural = '人類圖是你的人生使用說明書部分(索引值1)'

# 類型 = 你的天職部分
class YourType(HumanContentCommon):
      class Meta:
         verbose_name = '類型 = 你的天職(索引值2)'
         verbose_name_plural = '類型 = 你的天職(索引值2)'


