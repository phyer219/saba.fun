from django.db import models

# Create your models here.

class Shijing(models.Model):
    """诗经"""
    fixed_id = models.IntegerField(default=0)
    title = models.CharField(max_length=32, default='')
    chapter = models.CharField(max_length=32, default='')
    section = models.CharField(max_length=32, default='')
    content = models.TextField(max_length=8000, default='')

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title

class Ci(models.Model):
    """全宋词"""
    fixed_id = models.IntegerField(default=0)
    author = models.CharField(max_length=32, default='')
    paragraphs = models.TextField(max_length=8000, default='')
    rhythmic = models.CharField(max_length=32, default='')
    tags = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.rhythmic+self.tags
