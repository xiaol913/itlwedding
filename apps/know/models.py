from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class Know(models.Model):
    """
    婚礼须知
    """
    label = models.CharField(default="", max_length=40, verbose_name="标签", help_text="标签")
    desc = UEditorField(default="", verbose_name="内容", help_text="内容", width=1000, height=300,
                        filePath="images/know/img/", imagePath="images/know/img/", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "婚礼须知"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "婚礼须知"
