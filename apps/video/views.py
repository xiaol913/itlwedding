from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

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
        all_videos = VideoInfo.objects.all()

        return render(request, "video.html",{
            "videos": all_videos,
        })


class VideoInfoView(View):
    """
    视频列表页
    """
    def get(self, request, video_id):
        video = VideoInfo.objects.get(id=int(video_id))

        return render(request, "video_detail.html",{
            "video": video,
        })
