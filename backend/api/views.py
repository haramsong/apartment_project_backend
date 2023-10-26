from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AttachsSerializer, BoardContentsSerializer, DanjisSerializer, UserGroupsSerializer
from .models import Attachs, BoardContents, Danjis, UserGroups

# Create your views here.
class AttachsViewSet(viewsets.ModelViewSet):
    queryset = Attachs.objects.all()
    serializer_class = AttachsSerializer

class BoardContentsViewSet(viewsets.ModelViewSet):
    queryset = BoardContents.objects.all()
    serializer_class = BoardContentsSerializer

class DanjisViewSet(viewsets.ModelViewSet):
    queryset = Danjis.objects.all()
    serializer_class = DanjisSerializer

class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer
