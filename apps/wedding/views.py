
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import WeddingArea
from .serializer import WeddingAreaSerializer

# Create your views here.


class AreaListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        area = WeddingArea.objects.all()
        area_serializer = WeddingAreaSerializer(area, many=True)
        return Response(area_serializer.data)