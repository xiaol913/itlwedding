import json

from django.shortcuts import render
from django.views.generic import View

import requests
from rest_framework import viewsets, mixins

from .models import VideoInfo, VideoLabel
from .serializer import VideoInfoSerializer, VideoLabelSerializer
# Create your views here.


class VideoLabelViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
        婚礼视频label信息
    """
    queryset = VideoLabel.objects.all()
    serializer_class = VideoLabelSerializer


class VideoListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        婚礼视频列表页
    retrieve:
        婚礼视频详情
    """
    queryset = VideoInfo.objects.all()
    serializer_class = VideoInfoSerializer


class VideoListView(View):
    """
    视频列表页
    """
    def get(self, request):
        label_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/video_label/').text)
        videos_queryset = json.loads(requests.get(url='http://127.0.0.1:8000/api/video/').text)
        label = label_queryset[0]
        count = len(videos_queryset)

        return render(request, "video.html", {
            "label": label,
            "videos": videos_queryset,
            "count": count,
        })


class VideoInfoView(View):
    """
    视频列表页
    """
    def get(self, request, video_id):
        video = json.loads(requests.get(url='http://127.0.0.1:8000/api/video/' + str(video_id)).text)

        return render(request, "video-detail.html", {
            "video": video,
        })
