from django.db import models

class Mood(models.Model):
    status = models.CharField(max_length=20, null=False)
    
    class Meta:
            verbose_name = '回饋狀態'
            verbose_name_plural = '回饋狀態'

    def __str__(self):
        return self.status

class Post(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    message = models.TextField(null=False,verbose_name='回饋內容')
    del_pass = models.CharField(max_length=10,verbose_name='刪除的密碼')
    pub_time = models.DateTimeField(auto_now=True,verbose_name='回饋日期')
    enabled = models.BooleanField(default=False,verbose_name='是否可以回饋')
    
    class Meta:
        verbose_name = '回饋內容'
        verbose_name_plural = '回饋內容'

    def __str__(self):
        return self.message