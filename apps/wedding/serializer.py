from rest_framework import serializers
from .models import WeddingLabel, WeddingArea, WeddingInfo


class WeddingLabelSerializer(serializers.ModelSerializer):
    """
    海外婚礼
    """
    class Meta:
        model = WeddingLabel
        fields = "__all__"


class WeddingAreaSerializer(serializers.ModelSerializer):
    """
    海外区域
    """
    label = WeddingLabelSerializer()

    class Meta:
        model = WeddingArea
        fields = "__all__"


class WeddingInfoSerializer(serializers.ModelSerializer):
    """
    海外婚礼详情
    """
    area_name = WeddingAreaSerializer()

    class Meta:
        model = WeddingInfo
        fields = "__all__"
