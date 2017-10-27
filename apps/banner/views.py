from django.shortcuts import render
from django.views.generic import View

from rest_framework import viewsets, mixins

from .models import Banner
from .serializer import BannerSerializer
# Create your views here.


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        轮播图
    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerView(View):
    """
    轮播图
    """
    def get(self, request):
        banners = BannerSerializer(Banner.objects.all(), many=True).data

        return render(request, "index.html", {
            "banners": banners,
        })
