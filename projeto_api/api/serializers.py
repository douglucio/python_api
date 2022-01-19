from rest_framework import serializers
from .models import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name"]

class FluitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fluit
        fields = ["id", "name_fluit", "region_fluit" ]