from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class WeddingLabel(models.Model):
    """
    海外婚礼标签
    """
    label = models.CharField(default="", max_length=40, verbose_name="海外婚礼标签", help_text="海外婚礼标签")
    desc = models.TextField(default="", verbose_name="海外婚礼描述", help_text="海外婚礼描述", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "海外婚礼标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label


class WeddingArea(models.Model):
    """
    海外婚礼区域
    """
    code = models.CharField(default="", max_length=30, verbose_name="区域代码", help_text="区域代码")
    name = models.CharField(default="", max_length=30, verbose_name="区域名称", help_text="区域名称")
    flag = models.ImageField(upload_to="images/flags/", max_length=200, verbose_name="区域旗帜", help_text="区域旗帜")
    desc = models.TextField(default="", verbose_name="区域描述", help_text="区域描述")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "海外婚礼区域"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class WeddingInfo(models.Model):
    """
    海外婚礼详情页
    """
    area_code = models.ForeignKey(WeddingArea, verbose_name="婚礼区域", help_text="婚礼区域")
    place_id = models.CharField(default="", max_length=50, verbose_name="详情页ID", help_text="详情页ID")
    title = models.CharField(default="", max_length=50, verbose_name="场地名称", help_text="场地名称")
    label = models.CharField(default="", max_length=200, verbose_name="场地简述", help_text="场地简述")
    front_img = models.ImageField(upload_to="images/wedding/front/", max_length=200, verbose_name="封面图", help_text="封面图")
    hotel_info = UEditorField(default="", verbose_name="酒店介绍", help_text="酒店介绍", width=1000, height=300,
                              filePath="images/wedding/hotel/")
    place_info = UEditorField(default="", verbose_name="场地信息", help_text="场地信息", width=1000, height=300,
                              filePath="images/wedding/place/")
    server_info = UEditorField(default="", verbose_name="专业代订与其他服务", help_text="专业代订与其他服务", width=1000, height=300,
                               filePath="images/wedding/server/")
    book_info = UEditorField(default="", verbose_name="预约须知", help_text="预约须知", width=1000, height=300,
                             filePath="images/wedding/book/")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "海外婚礼详情页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
