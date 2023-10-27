from rest_framework import viewsets
from .serializers import AttachsSerializer
from .models import Attachs


class AttachsViewSet(viewsets.ModelViewSet):
    queryset = Attachs.objects.all()
    serializer_class = AttachsSerializer
