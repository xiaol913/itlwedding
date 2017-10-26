from rest_framework import serializers
from .models import WeddingLabel, WeddingArea, WeddingInfo, WeddingInfoImage


class WeddingLabelSerializer(serializers.ModelSerializer):
    """
    海外婚礼
    """
    class Meta:
        model = WeddingLabel
        fields = "__all__"


class WeddingInfoImageSerializer(serializers.ModelSerializer):
    """
    海外婚礼详情图片
    """
    class Meta:
        model = WeddingInfoImage
        fields = ("img",)


class WeddingInfoSerializer(serializers.ModelSerializer):
    """
    海外婚礼详情
    """
    images = WeddingInfoImageSerializer(many=True)

    class Meta:
        model = WeddingInfo
        fields = "__all__"


class WeddingAreaSerializer(serializers.ModelSerializer):
    """
    海外区域
    """
    class Meta:
        model = WeddingArea
        fields = "__all__"

