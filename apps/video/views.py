import json

from django.shortcuts import render
from django.views.generic import View

import requests
from rest_framework import viewsets

from .models import VideoInfo
from .serializer import VideoInfoSerializer
from wedding.views import ListInfoPagination
# Create your views here.


class VideoListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        婚礼视频列表页、分页
    retrieve:
        婚礼视频详情
    """
    queryset = VideoInfo.objects.all()
    serializer_class = VideoInfoSerializer
    pagination_class = ListInfoPagination


class VideoListView(View):
    """
    视频列表页
    """
    def get(self, request):
        all_videos = json.loads(requests.get(url='http://127.0.0.1:8000/api/video/').text)
        count = all_videos['count']
        videos = all_videos['results']

        return render(request, "video.html", {
            "videos": videos,
            "count": count,
        })


class VideoInfoView(View):
    """
    视频列表页
    """
    def get(self, request, video_id):
        video = json.loads(requests.get(url='http://127.0.0.1:8000/api/video/' + str(video_id)).text)

        return render(request, "video_detail.html", {
            "video": video,
        })
