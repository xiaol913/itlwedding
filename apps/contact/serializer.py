# _*_ coding=utf8 _*_
from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    联系我们
    """
    class Meta:
        model = Contact
        fields = "__all__"
