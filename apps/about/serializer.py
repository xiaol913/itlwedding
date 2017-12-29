# _*_ coding=utf8 _*_
from rest_framework import serializers

from .models import About


class AboutSerializer(serializers.ModelSerializer):
    """
    关于我们
    """
    class Meta:
        model = About
        fields = "__all__"
