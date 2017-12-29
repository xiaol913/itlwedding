# _*_ coding=utf8 _*_
from django.conf.urls import url
from .views import KnowView

urlpatterns = [
    # 视频列表页
    url(r'^$', KnowView.as_view(), name="know"),
]
