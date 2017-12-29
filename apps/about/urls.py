# _*_ coding=utf8 _*_
from django.conf.urls import url
from .views import AboutView

urlpatterns = [
    # 视频列表页
    url(r'^$', AboutView.as_view(), name="about"),
]
