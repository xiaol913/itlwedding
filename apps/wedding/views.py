from django.shortcuts import render
from django.views import View

from django_filters.rest_framework import DjangoFilterBackend

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


class WeddingAreaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        海外婚礼区域列表
    retrieve:
        海外婚礼区域信息
    """
    queryset = WeddingArea.objects.all()
    serializer_class = WeddingAreaSerializer


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


class WeddingListView(View):
    """
    海外婚礼列表
    """
    def get(self, request):
        label = WeddingLabelSerializer(WeddingLabel.objects.all(), many=True).data[0]
        areas = WeddingAreaSerializer(WeddingArea.objects.all(), many=True).data

        area_id = request.GET.get('area_id')
        if area_id:
            area_id = int(area_id)
            wedding = WeddingInfoSerializer(WeddingInfo.objects.filter(area_id=area_id), many=True).data
        else:
            wedding = WeddingInfoSerializer(WeddingInfo.objects.all(), many=True).data

        count = len(wedding)

        return render(request, "wedding.html", {
            "areas": areas,
            "weddings": wedding,
            "label": label,
            "count": count,
            "area_id": area_id,
        })


class WeddingInfoView(View):
    """
    海外婚礼详情
    """
    def get(self, request, wedding_id):
        wedding = WeddingInfoSerializer(WeddingInfo.objects.get(id=int(wedding_id))).data
        images = wedding['images']
        count = len(images)

        return render(request, "wedding-detail.html", {
            "wedding": wedding,
            "images": images,
            "count": count,
        })

