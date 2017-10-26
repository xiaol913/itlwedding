# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import WeddingListView, WeddingInfoView

urlpatterns = [
    # 视频列表页
    url(r'^$', WeddingListView.as_view(), name="wedding"),
    # 视频详情页
    url(r'^(?P<wedding_id>\d+)/$', WeddingInfoView.as_view(), name="wedding_detail"),
]
