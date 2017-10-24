from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class PhotoLabel(models.Model):
    """
    环球旅拍
    """
    name = models.CharField(default="环球旅拍", max_length=40, verbose_name="该大类名称", help_text="该大类名称")
    label = models.CharField(default="", max_length=40, verbose_name="标签", help_text="标签")
    desc = models.TextField(default="", verbose_name="描述", help_text="描述", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "环球旅拍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class PhotoInfo(models.Model):
    """
    环球旅拍详情页
    """
    label = models.ForeignKey(PhotoLabel, verbose_name="环球旅拍", help_text="环球旅拍")
    name = models.CharField(default="", max_length=50, verbose_name="地点名称", help_text="地点名称")
    desc = models.CharField(default="", max_length=200, verbose_name="地点简述", help_text="地点简述")
    front_img = models.ImageField(upload_to="images/photo/front/", max_length=200, verbose_name="封面图", help_text="封面图")
    photo_info = UEditorField(default="", verbose_name="旅拍详情", help_text="旅拍详情", width=1000, height=300,
                              filePath="images/photo/img/", imagePath="images/photo/img/")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "环球旅拍详情页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
