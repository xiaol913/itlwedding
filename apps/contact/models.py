from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.


class Contact(models.Model):
    """
    联系我们
    """
    desc = UEditorField(default="", verbose_name="内容", help_text="内容", width=1000, height=300,
                        filePath="images/contact/img/", imagePath="images/contact/img/", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "联系我们"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "联系我们"
