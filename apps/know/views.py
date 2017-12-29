from django.shortcuts import render
from django.views.generic import View

from rest_framework import viewsets, mixins

from .models import Know
from .serializer import KnowSerializer
# Create your views here.


class KnowViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        婚礼须知
    """
    queryset = Know.objects.all()
    serializer_class = KnowSerializer


class KnowView(View):
    """
    婚礼须知
    """
    def get(self, request):
        knows = KnowSerializer(Know.objects.all(), many=True).data

        return render(request, "know.html", {
            "knows": knows,
        })
