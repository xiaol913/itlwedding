from django.shortcuts import render
from django.views.generic import View

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
        label = VideoLabelSerializer(VideoLabel.objects.all(), many=True).data[0]
        videos = VideoInfoSerializer(VideoInfo.objects.all(), many=True).data
        count = len(videos)

        return render(request, "video.html", {
            "label": label,
            "videos": videos,
            "count": count,
        })


class VideoInfoView(View):
    """
    视频列表页
    """
    def get(self, request, video_id):
        video = VideoInfoSerializer(VideoInfo.objects.get(id=int(video_id))).data

        return render(request, "video-detail.html", {
            "video": video,
        })
