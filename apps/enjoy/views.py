from rest_framework import viewsets

from .models import EnjoyInfo
from .serializer import EnjoyInfoSerializer
from wedding.views import ListInfoPagination
# Create your views here.


class EnjoyListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        海外婚礼列表页、分页
    retrieve:
        海外婚礼详情
    """
    queryset = EnjoyInfo.objects.all()
    serializer_class = EnjoyInfoSerializer
    pagination_class = ListInfoPagination
