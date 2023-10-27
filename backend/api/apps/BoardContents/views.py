from rest_framework import viewsets
from .serializers import BoardContentsSerializer
from .models import BoardContents


class BoardContentsViewSet(viewsets.ModelViewSet):
    queryset = BoardContents.objects.all()
    serializer_class = BoardContentsSerializer