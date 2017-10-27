"""itlwedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from itlwedding.settings import MEDIA_ROOT
from wedding.views import WeddingListViewSet, WeddingLabelViewSet, WeddingAreaViewSet
from photo.views import PhotoListViewSet, PhotoLabelViewSet
from enjoy.views import EnjoyListViewSet, EnjoyLabelViewSet
from video.views import VideoListViewSet, VideoLabelViewSet
from banner.views import BannerView, BannerViewSet

import xadmin

router = DefaultRouter()

# 配置婚礼视频url
router.register(r'video', VideoListViewSet, base_name="婚礼视频")
# 配置婚礼视频Label url
router.register(r'video_label', VideoLabelViewSet, base_name="婚礼视频标签")
# 配置客片欣赏url
router.register(r'enjoy', EnjoyListViewSet, base_name="客片欣赏")
# 配置客片欣赏Label url
router.register(r'enjoy_label', EnjoyLabelViewSet, base_name="客片欣赏标签")
# 配置环球旅拍url
router.register(r'photo', PhotoListViewSet, base_name="环球旅拍")
# 配置环球旅拍Label url
router.register(r'photo_label', PhotoLabelViewSet, base_name="环球旅拍标签")
# 配置海外婚礼url
router.register(r'wedding', WeddingListViewSet, base_name="海外婚礼")
# 配置海外婚礼url
router.register(r'wedding_area', WeddingAreaViewSet, base_name="海外婚礼区域")
# 配置环球旅拍Label url
router.register(r'wedding_label', WeddingLabelViewSet, base_name="海外婚礼标签")
# 配置轮播图url
router.register(r'banner', BannerViewSet, base_name="轮播图")

urlpatterns = [
    # Xadmin管理页面
    url(r'^xadmin/', xadmin.site.urls),

    # DRFApi接口
    url(r'docs/', include_docs_urls(title="Itlwedding-API")),

    # router注册
    url(r'^api/', include(router.urls)),

    # 富文本
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    # 媒体页面
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 主页
    url(r'^$', BannerView.as_view(), name="index"),

    # 关于我们
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name="about"),

    # 联系我们
    url(r'^contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),

    # 须知页面
    url(r'^know/', TemplateView.as_view(template_name="know.html"), name="know"),

    # 婚礼视频url配置
    url(r'^video/', include('video.urls'), name="video"),

    # 客片欣赏url配置
    url(r'^enjoy/', include('enjoy.urls'), name="enjoy"),

    # 环球旅拍url配置
    url(r'^photo/', include('photo.urls'), name="photo"),

    # 海外婚礼url配置
    url(r'^wedding/', include('wedding.urls'), name="wedding"),
]
