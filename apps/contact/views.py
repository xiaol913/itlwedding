from django.shortcuts import render
from django.views.generic import View

from rest_framework import viewsets, mixins

from .models import Contact
from .serializer import ContactSerializer
# Create your views here.


class ContactViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        联系我们
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactView(View):
    """
    联系我们
    """
    def get(self, request):
        contact = ContactSerializer(Contact.objects.all(), many=True).data[0]

        return render(request, "contact.html", {
            "contact": contact,
        })
