from datetime import datetime

from django.db import models

# Create your models here.


class Banner(models.Model):
    """
    轮播图
    """
    image = models.ImageField(upload_to='images/banner/', max_length=200, verbose_name="轮播图", help_text="轮播图")
    title = models.CharField(default="", max_length=50, verbose_name="标题", help_text="标题")
    label = models.CharField(default="", max_length=100, verbose_name="标签", help_text="标签")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
