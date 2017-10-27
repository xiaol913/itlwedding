from django.shortcuts import render
from django.views.generic import View

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
        photos = PhotoInfoSerializer(PhotoInfo.objects.all(), many=True).data
        label = PhotoLabelSerializer(PhotoLabel.objects.all(), many=True).data[0]
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
        photo = PhotoInfoSerializer(PhotoInfo.objects.get(id=int(photo_id))).data
        images = photo['images']
        count = len(images)

        return render(request, "photo-detail.html", {
            "photo": photo,
            "images": images,
            "count": count,
        })
