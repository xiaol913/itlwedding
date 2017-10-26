import json

from django.shortcuts import render
from django.views.generic import View

import requests
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
        enjoy_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/enjoy/').text)
        label_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/enjoy_label/').text)
        label = label_queryset[0]
        count = len(enjoy_queryset)

        return render(request, "enjoy.html", {
            "enjoys": enjoy_queryset,
            "label": label,
            "count": count,
        })


class EnjoyInfoView(View):
    """
    客片详情页
    """
    def get(self, request, enjoy_id):
        enjoy = json.loads(requests.get(url='http://127.0.0.1:8000/api/enjoy/' + str(enjoy_id)).text)
        images = enjoy['images']
        count = len(images)

        return render(request, "enjoy-detail.html", {
            "enjoy": enjoy,
            "images": images,
            "count": count,
        })
