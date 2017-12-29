from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class About(models.Model):
    """
    关于我们
    """
    desc = UEditorField(default="", verbose_name="内容", help_text="内容", width=1000, height=300,
                        filePath="images/about/img/", imagePath="images/about/img/", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "关于我们"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "关于我们"
