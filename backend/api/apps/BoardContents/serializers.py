from rest_framework import serializers
from .models import BoardContents


class BoardContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardContents
        fields = "__all__"
