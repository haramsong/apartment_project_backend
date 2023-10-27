from rest_framework import viewsets
from .serializers import UserGroupsSerializer
from .models import UserGroups


class UserGroupsViewSet(viewsets.ModelViewSet):
    queryset = UserGroups.objects.all()
    serializer_class = UserGroupsSerializer
