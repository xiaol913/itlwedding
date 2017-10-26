# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import VideoLabel, VideoInfo


class VideoLabelSerializer(serializers.ModelSerializer):
    """
    婚礼视频
    """
    class Meta:
        model = VideoLabel
        fields = ("name", "label", "desc")


class VideoInfoSerializer(serializers.ModelSerializer):
    """
    婚礼视频详情页
    """
    class Meta:
        model = VideoInfo
        fields = "__all__"
