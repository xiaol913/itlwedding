# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import PhotoLabel, PhotoInfo, PhotoInfoImage


class PhotoLabelSerializer(serializers.ModelSerializer):
    """
    环球旅拍
    """
    class Meta:
        model = PhotoLabel
        fields = "__all__"


class PhotoInfoImageSerializer(serializers.ModelSerializer):
    """
    环球旅拍照片
    """
    class Meta:
        model = PhotoInfoImage
        fields = ("img",)


class PhotoInfoSerializer(serializers.ModelSerializer):
    """
    环球旅拍详情页
    """
    images = PhotoInfoImageSerializer(many=True)

    class Meta:
        model = PhotoInfo
        fields = "__all__"
