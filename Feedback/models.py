from django.db import models

class Value(models.Model):
      status=models.CharField(max_length=20,null=False)

      def __str__(self):
            return self.status

class Post(models.Model):
      value=models.ForeignKey('Value',on_delete=models.CASCADE)
      user_name=models.CharField(max_length=20,default='匿名者',verbose_name='您的代稱')
      message=models.TextField(null=False,verbose_name='回饋內容')
      del_pass=models.CharField(max_length=20)
      pub_time=models.DateTimeField(auto_now=True,verbose_name='發布日期')
      enabled=models.BooleanField(default=False,verbose_name='是否可發布')

      def __str__(self):
            return self.message