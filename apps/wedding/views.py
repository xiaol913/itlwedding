import json

from django.shortcuts import render
from django.views import View

from django_filters.rest_framework import DjangoFilterBackend
import requests
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from .models import WeddingInfo, WeddingArea, WeddingLabel
from .serializer import WeddingInfoSerializer, WeddingLabelSerializer, WeddingAreaSerializer
# Create your views here.


class ListInfoPagination(PageNumberPagination):
    """
    分页配置
    """
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'per_page'


class WeddingLabelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        海外婚礼label
    """
    queryset = WeddingLabel.objects.all()
    serializer_class = WeddingLabelSerializer


class WeddingListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        海外婚礼列表页、分页
    retrieve:
        海外婚礼详情
    """
    queryset = WeddingInfo.objects.all()
    serializer_class = WeddingInfoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('area_id',)


class WeddingAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        海外婚礼区域列表
    retrieve:
        海外婚礼区域信息
    """
    queryset = WeddingArea.objects.all()
    serializer_class = WeddingAreaSerializer


class WeddingListView(View):
    """
    海外婚礼列表
    """
    def get(self, request):
        area_id = request.GET.get('area_id')
        label_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/wedding_label/').text)
        area_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/wedding_area/').text)
        wedding_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/wedding/').text)
        if area_id:
            wedding_queryset = json.loads(requests.get(
                url='http://127.0.0.1:8000/api/wedding/?area_id=' + area_id).text)
            area_id = int(area_id)

        count = len(wedding_queryset)
        label = label_queryset[0]

        return render(request, "wedding.html", {
            "areas": area_queryset,
            "weddings": wedding_queryset,
            "label": label,
            "count": count,
            "area_id": area_id,
        })


class WeddingInfoView(View):
    """
    海外婚礼详情
    """
    def get(self, request, wedding_id):
        wedding_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/wedding/' + str(wedding_id)).text)
        images = wedding_queryset['images']
        count = len(images)

        return render(request, "wedding-detail.html", {
            "wedding": wedding_queryset,
            "images": images,
            "count": count,
        })

