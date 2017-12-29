from django.shortcuts import render
from django.views.generic import View

from rest_framework import viewsets, mixins

from .models import About
from .serializer import AboutSerializer
# Create your views here.


class AboutViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        关于我们
    """
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutView(View):
    """
    关于我们
    """
    def get(self, request):
        about = AboutSerializer(About.objects.all(), many=True).data[0]

        return render(request, "about.html", {
            "about": about,
        })
