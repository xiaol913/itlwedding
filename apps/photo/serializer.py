# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import PhotoLabel, PhotoInfo


class PhotoLabelSerializer(serializers.ModelSerializer):
    """
    环球旅拍
    """
    class Meta:
        model = PhotoLabel
        fields = "__all__"


class PhotoInfoSerializer(serializers.ModelSerializer):
    """
    环球旅拍详情页
    """
    label = PhotoLabelSerializer()

    class Meta:
        model = PhotoInfo
        fields = "__all__"
