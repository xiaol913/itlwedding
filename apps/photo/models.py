from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class PhotoLabel(models.Model):
    """
    环球旅拍标签
    """
    label = models.CharField(default="", max_length=40, verbose_name="环球旅拍标签", help_text="环球旅拍标签")
    desc = models.TextField(default="", verbose_name="环球旅拍描述", help_text="环球旅拍描述", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "环球旅拍标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label


class PhotoInfo(models.Model):
    """
    环球旅拍详情页
    """
    photo_id = models.CharField(default="", max_length=50, verbose_name="详情页ID", help_text="详情页ID")
    title = models.CharField(default="", max_length=50, verbose_name="地点名称", help_text="地点名称")
    label = models.CharField(default="", max_length=200, verbose_name="地点简述", help_text="地点简述")
    front_img = models.ImageField(upload_to="images/hotel/front/", max_length=200, verbose_name="封面图", help_text="封面图")
    photo_info = UEditorField(default="", verbose_name="旅拍详情", help_text="旅拍详情", width=1000, height=300,
                              filePath="images/hotel/img/")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "环球旅拍详情页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
