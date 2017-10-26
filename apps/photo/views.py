import json

from django.shortcuts import render
from django.views.generic import View

import requests

from rest_framework import viewsets, mixins

from .models import PhotoInfo, PhotoLabel
from .serializer import PhotoInfoSerializer, PhotoLabelSerializer
# Create your views here.


class PhotoLabelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        环球旅拍label
    """
    queryset = PhotoLabel.objects.all()
    serializer_class = PhotoLabelSerializer


class PhotoListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        环球旅拍列表页、分页
    retrieve:
        环球旅拍详情
    """
    queryset = PhotoInfo.objects.all()
    serializer_class = PhotoInfoSerializer


class PhotoListView(View):
    """
    环球旅拍列表页
    """
    def get(self, request):
        photos = json.loads(requests.get(url='http://127.0.0.1:8000/api/photo/').text)
        label = json.loads(requests.get(url='http://127.0.0.1:8000/api/photo_label/').text)[0]
        count = len(photos)

        return render(request, "photo.html", {
            "photos": photos,
            "label": label,
            "count": count,
        })


class PhotoInfoView(View):
    """
    环球旅拍详情页
    """
    def get(self, request, photo_id):
        photo = json.loads(requests.get(url='http://127.0.0.1:8000/api/photo/' + str(photo_id)).text)
        images = photo['images']
        count = len(images)

        return render(request, "photo-detail.html", {
            "photo": photo,
            "images": images,
            "count": count,
        })
