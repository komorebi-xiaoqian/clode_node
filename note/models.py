from django.db import models

# Create your models here.
from user.models import User


class Note(models.Model):
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isActivate = models.BooleanField("是否删除", default=True)

    def __str__(self):
        return f'{self.id}-{self.title}-{self.content}-{self.created_time}-{self.updated_time}-{self.user}'

    class Meta:
        db_table = 'note'
