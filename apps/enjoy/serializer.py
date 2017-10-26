# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import EnjoyLabel, EnjoyInfo, EnjoyInfoImage


class EnjoyLabelSerializer(serializers.ModelSerializer):
    """
    客片欣赏
    """
    class Meta:
        model = EnjoyLabel
        fields = ("name", "label", "desc")


class EnjoyInfoImageSerializer(serializers.ModelSerializer):
    """
    客片详情图片
    """
    class Meta:
        model = EnjoyInfoImage
        fields = ("img",)


class EnjoyInfoSerializer(serializers.ModelSerializer):
    """
    客片欣赏详情页
    """
    images = EnjoyInfoImageSerializer(many=True)

    class Meta:
        model = EnjoyInfo
        fields = "__all__"
