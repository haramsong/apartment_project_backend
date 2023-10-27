from rest_framework import serializers
from .models import UserGroups


class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroups
        fields = "__all__"
