from rest_framework import serializers
from .models import Attachs, BoardContents, Danjis, UserGroups

class AttachsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachs
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')

class BoardContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardContents
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')

class DanjisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Danjis
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')

class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroups
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')