# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import VideoListView, VideoInfoView

urlpatterns = [
    # 视频列表页
    url(r'^$', VideoListView.as_view(), name="video"),
    # 视频详情页
    url(r'^(?P<video_id>\d+)/$', VideoInfoView.as_view(), name="video_detail"),
]
