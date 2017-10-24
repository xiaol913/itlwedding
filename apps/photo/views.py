from rest_framework import viewsets

from .models import PhotoInfo
from .serializer import PhotoInfoSerializer
from wedding.views import ListInfoPagination
# Create your views here.


class PhotoListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        海外婚礼列表页、分页
    retrieve:
        海外婚礼详情
    """
    queryset = PhotoInfo.objects.all()
    serializer_class = PhotoInfoSerializer
    pagination_class = ListInfoPagination
