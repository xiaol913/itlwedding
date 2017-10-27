# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Banner


class BannerSerializer(serializers.ModelSerializer):
    """
    轮播图
    """
    class Meta:
        model = Banner
        fields = "__all__"
