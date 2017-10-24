from datetime import datetime

from django.db import models
# Create your models here.


class VideoLabel(models.Model):
    """
    婚礼视频
    """
    name = models.CharField(default="婚礼视频", max_length=40, verbose_name="该大类名称", help_text="该大类名称")
    label = models.CharField(default="", max_length=40, verbose_name="标签", help_text="标签")
    desc = models.TextField(default="", verbose_name="描述", help_text="描述")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "婚礼视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VideoInfo(models.Model):
    """
    婚礼视频详情页
    """
    label = models.ForeignKey(VideoLabel, verbose_name="婚礼视频", help_text="婚礼视频")
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
