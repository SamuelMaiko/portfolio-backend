from rest_framework import serializers
from .models import Service, KeyFeature


class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at'
        ]


class ServiceSerializer(serializers.ModelSerializer):
    keyfeatures = KeyFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = [
            'id',
            'badge',
            'name',
            'description',
            'sequence',
            'keyfeatures',
            'created_at',
            'updated_at'
        ]
