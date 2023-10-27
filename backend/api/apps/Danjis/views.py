from rest_framework import viewsets
from .serializers import DanjisSerializer
from .models import Danjis


class DanjisViewSet(viewsets.ModelViewSet):
    queryset = Danjis.objects.all()
    serializer_class = DanjisSerializer
