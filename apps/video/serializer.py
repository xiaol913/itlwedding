# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import VideoLabel, VideoInfo


class VideoLabelSerializer(serializers.ModelSerializer):
    """
    婚礼视频
    """
    class Meta:
        model = VideoLabel
        fields = "__all__"


class VideoInfoSerializer(serializers.ModelSerializer):
    """
    婚礼视频详情页
    """
    label = VideoLabelSerializer()

    class Meta:
        model = VideoInfo
        fields = "__all__"
