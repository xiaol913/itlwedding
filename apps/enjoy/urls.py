# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import EnjoyListView, EnjoyInfoView

urlpatterns = [
    # 视频列表页
    url(r'^$', EnjoyListView.as_view(), name="enjoy"),
    # 视频详情页
    url(r'^(?P<enjoy_id>\d+)/$', EnjoyInfoView.as_view(), name="enjoy_detail"),
]
