from rest_framework import serializers
from .models import Attachs

class AttachsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachs
        fields = ("__all__")
        #fields = ('name', 'description', 'cost')