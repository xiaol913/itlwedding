from rest_framework import serializers


class WeddingAreaSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    flag = serializers.ImageField()
