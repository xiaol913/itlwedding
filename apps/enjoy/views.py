from django.shortcuts import render
from django.views.generic import View

from rest_framework import viewsets, mixins

from .models import EnjoyInfo, EnjoyLabel
from .serializer import EnjoyInfoSerializer, EnjoyLabelSerializer
# Create your views here.


class EnjoyLabelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
        客片标签
    """
    queryset = EnjoyLabel.objects.all()
    serializer_class = EnjoyLabelSerializer


class EnjoyListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        客片列表页
    retrieve:
        客片详情
    """
    queryset = EnjoyInfo.objects.all()
    serializer_class = EnjoyInfoSerializer


class EnjoyListView(View):
    """
    客片列表页
    """
    def get(self, request):
        enjoys = EnjoyInfoSerializer(EnjoyInfo.objects.all(), many=True).data
        count = len(enjoys)

        label = EnjoyLabelSerializer(EnjoyLabel.objects.all(), many=True).data[0]

        return render(request, "enjoy.html", {
            "enjoys": enjoys,
            "label": label,
            "count": count,
        })


class EnjoyInfoView(View):
    """
    客片详情页
    """
    def get(self, request, enjoy_id):
        enjoy = EnjoyInfoSerializer(EnjoyInfo.objects.get(id=enjoy_id)).data
        images = enjoy['images']
        count = len(images)

        return render(request, "enjoy-detail.html", {
            "enjoy": enjoy,
            "images": images,
            "count": count,
        })
