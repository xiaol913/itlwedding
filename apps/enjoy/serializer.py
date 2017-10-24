# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import EnjoyLabel, EnjoyInfo


class EnjoyLabelSerializer(serializers.ModelSerializer):
    """
    客片欣赏
    """
    class Meta:
        model = EnjoyLabel
        fields = "__all__"


class EnjoyInfoSerializer(serializers.ModelSerializer):
    """
    客片欣赏详情页
    """
    label = EnjoyLabelSerializer()

    class Meta:
        model = EnjoyInfo
        fields = "__all__"
