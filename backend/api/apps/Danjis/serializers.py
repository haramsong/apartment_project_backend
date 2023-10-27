from rest_framework import serializers
from .models import Danjis


class DanjisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Danjis
        fields = "__all__"
