from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import WeddingInfo, WeddingArea
from .serializer import WeddingInfoSerializer
# Create your views here.


class ListInfoPagination(PageNumberPagination):
    """
    分页配置
    """
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'per_page'


class WeddingListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        海外婚礼列表页、分页
    retrieve:
        海外婚礼详情
    """
    queryset = WeddingInfo.objects.all()
    serializer_class = WeddingInfoSerializer
    pagination_class = ListInfoPagination


# class WeddingAreaViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     list:
#         海外婚礼区域列表
#     retrieve:
#         海外婚礼区域信息
#     """
#     queryset = WeddingArea.objects.all()
#     serializer_class = WeddingAreaSerializer
