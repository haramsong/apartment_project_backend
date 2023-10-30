from rest_framework import serializers
from .models import BoardContents
from ..Attachs.serializers import AttachsSerializer


class BoardContentsSerializer(serializers.ModelSerializer):
    attachs = AttachsSerializer(many=True)
    class Meta:
        model = BoardContents
        fields = "__all__"
