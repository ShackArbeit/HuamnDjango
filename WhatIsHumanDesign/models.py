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

# 人生角色 的部分
class YourRole(HumanContentCommon):
      class Meta:
         verbose_name = '人生角色(索引值3)'
         verbose_name_plural = '人生角色(索引值3)'


# 內在權威 = 做決定的方法 的部分
class YourAuth(HumanContentCommon):
      class Meta:
         verbose_name = '內在權威 = 做決定的方法(索引值4)'
         verbose_name_plural = '內在權威 = 做決定的方法(索引值4)'

# 能量中心 = 你的強弱 的部分
class YourEnergy(HumanContentCommon):
       class Meta:
         verbose_name = '能量中心 = 你的強弱(索引值5)'
         verbose_name_plural = '能量中心 = 你的強弱(索引值5)'

# 通道 = 你的天賦 的部分
class YourRoad(HumanContentCommon):
      class Meta:
         verbose_name = '通道 = 你的天賦(索引值6)'
         verbose_name_plural = '通道 = 你的天賦(索引值6)'

# 輪迴交叉 = 你的命運 的部分
class YourMin(HumanContentCommon):
      class Meta:
         verbose_name = '輪迴交叉 = 你的命運(索引值7)'
         verbose_name_plural = '輪迴交叉 = 你的命運(索引值7)'

# # Ra Uru Hu = 引進人類圖 的部分
# class HumanFather(HumanContentCommon):
#       class Meta:
#          verbose_name = 'Ra Uru Hu = 引進人類圖(索引值8)'
#          verbose_name_plural = 'Ra Uru Hu = 引進人類圖(索引值8)'
