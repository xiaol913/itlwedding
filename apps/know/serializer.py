# _*_ coding=utf8 _*_
from rest_framework import serializers

from .models import Know


class KnowSerializer(serializers.ModelSerializer):
    """
    婚礼须知
    """
    class Meta:
        model = Know
        fields = "__all__"
