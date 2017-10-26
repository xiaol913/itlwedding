# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PhotoListView, PhotoInfoView

urlpatterns = [
    # 视频列表页
    url(r'^$', PhotoListView.as_view(), name="photo"),
    # 视频详情页
    url(r'^(?P<photo_id>\d+)/$', PhotoInfoView.as_view(), name="photo_detail"),
]
