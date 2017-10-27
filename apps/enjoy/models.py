from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.


class EnjoyLabel(models.Model):
    """
    客片欣赏
    """
    name = models.CharField(default="客片欣赏", max_length=40, verbose_name="该大类名称", help_text="该大类名称")
    label = models.CharField(default="", max_length=40, verbose_name="标签", help_text="标签")
    desc = models.TextField(default="", verbose_name="描述", help_text="描述", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "客片欣赏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class EnjoyInfo(models.Model):
    """
    客片欣赏详情页
    """
    title = models.CharField(default="", max_length=50, verbose_name="客片标题", help_text="客片标题")
    desc = models.CharField(default="", max_length=200, verbose_name="客片简述", help_text="客片简述", null=True, blank=True)
    front_img = models.ImageField(upload_to="images/enjoy/front/", max_length=200, verbose_name="封面图", help_text="封面图")
    enjoy_info = UEditorField(default="", verbose_name="客片故事", help_text="客片故事", width=1000, height=300,
                              filePath="images/enjoy/img/", imagePath="images/enjoy/img/", null=True, blank=True)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "客片欣赏详情页"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_images_nums(self):
        return self.images.all().count()

    get_images_nums.short_description = "图片数"


class EnjoyInfoImage(models.Model):
    """
    客片详情页照片
    """
    name = models.ForeignKey(EnjoyInfo, verbose_name="详情", help_text="详情", related_name="images")
    img = models.ImageField(upload_to="images/enjoy/img/")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")

    class Meta:
        verbose_name = "客片详情页照片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "客片详情页照片"
