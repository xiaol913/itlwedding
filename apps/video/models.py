from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.


class VideoLabel(models.Model):
    """
    婚礼视频标签
    """
    label = models.CharField(default="", max_length=40, verbose_name="婚礼视频标签", help_text="婚礼视频标签")
    desc = models.TextField(default="", verbose_name="婚礼视频描述", help_text="婚礼视频描述")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "婚礼视频标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label


class VideoInfo(models.Model):
    """
    婚礼视频详情页
    """
    video_id = models.CharField(default="", max_length=50, verbose_name="详情页ID", help_text="详情页ID")
    title = models.CharField(default="", max_length=50, verbose_name="视频标题", help_text="视频标题")
    front_img = models.ImageField(upload_to="images/video/front/", max_length=200, verbose_name="封面图", help_text="封面图")
    video_info = models.TextField(default="", max_length=200, verbose_name="视频描述", help_text="视频描述")
    video_url = models.URLField(default="", max_length=200, verbose_name="视频链接", help_text="视频链接")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "婚礼视频详情页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
