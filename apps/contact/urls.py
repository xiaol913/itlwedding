# _*_ coding=utf8 _*_
from django.conf.urls import url
from .views import ContactView

urlpatterns = [
    # 视频列表页
    url(r'^$', ContactView.as_view(), name="contact"),
]
