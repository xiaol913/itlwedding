from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.


class EnjoyLabel(models.Model):
    """
    客片欣赏标签
    """
    label = models.CharField(default="", max_length=40, verbose_name="客片欣赏标签", help_text="客片欣赏标签")
    desc = models.TextField(default="", verbose_name="客片欣赏描述", help_text="客片欣赏描述", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "客片欣赏标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.label


class EnjoyInfo(models.Model):
    """
    客片欣赏详情页
    """
    enjoy_id = models.CharField(default="", max_length=50, verbose_name="详情页ID", help_text="详情页ID")
    title = models.CharField(default="", max_length=50, verbose_name="客片标题", help_text="客片标题")
    label = models.CharField(default="", max_length=200, verbose_name="客片简述", help_text="客片简述", null=True, blank=True)
    front_img = models.ImageField(upload_to="images/enjoy/front/", max_length=200, verbose_name="封面图", help_text="封面图")
    enjoy_info = UEditorField(default="", verbose_name="客片故事", help_text="客片故事", width=1000, height=300,
                              filePath="images/enjoy/img/")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "客片欣赏详情页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
