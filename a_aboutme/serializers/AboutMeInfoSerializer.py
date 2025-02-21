from rest_framework import serializers
from a_aboutme.models import AboutMeInfo

class AboutMeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMeInfo
        fields = [
            'id',
            'photo_url',
            'description',
            'created_at',
            'updated_at'
        ]
