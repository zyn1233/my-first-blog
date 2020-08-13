from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField(max_length=200, verbose_name='标题')
    text = models.TextField(verbose_name='内容')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='创建时间')
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name='发布时间')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '池塘'
        verbose_name_plural = '我的博客'
